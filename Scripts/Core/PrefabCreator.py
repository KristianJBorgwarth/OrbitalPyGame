import json
import pygame
from Scripts.Core.GameObject import GameObject
from Scripts.Components.AstroidComponent import Astroid
from Scripts.Components.CoreComponents import Transform, Animator
from Scripts.Components.PhysicsComponents import Rigidbody
from Scripts.Components.PlayerComponents import Player


def create_prefab_instance(go: GameObject, go_name, prefab_file_path):
    data = json.dumps(_serialize_gameobject(go=go, go_name=go_name), indent=4)

    with open(prefab_file_path, "w") as f:
        f.write(data)


def load_prefab_instance(world, file_path):
    # Open the JSON file specified by file_path
    with open(file_path, 'r') as file:
        # Load the JSON data into a Python dictionary
        data = json.load(file)

    # Create a new GameObject instance using data from the JSON file
    go = GameObject(data["initial_position"]["x"], data["initial_position"]["y"], data['image_path'], world, )

    # Loop through the components defined in the JSON file
    for component_data in data['components']:
        # Determine the type of component based on the 'type' field in the JSON data
        component_type = component_data['type']

        # Create a new component based on the data in the JSON file and add it to the GameObject
        if component_type == 'Transform':
            transform = Transform.deserialize(component_data, go)
            transform.position = pygame.math.Vector2(data['initial_position']['x'], data['initial_position']['y'])
            go.add_component(transform)
        elif component_type == 'Rigidbody':
            rigidbody = Rigidbody.deserialize(component_data, go)
            go.add_component(rigidbody)
        elif component_type == 'Player':
            player = Player(go)
            go.add_component(player)
        elif component_type == 'Animator':
            animator = Animator.deserialize(component_data, go)
            go.add_component(animator)

        elif component_type == 'Actor':
            astroid = Astroid(go)
            go.add_component(astroid)
        else:
            # If the component type is not recognized, raise an error
            raise ValueError(f'Invalid component type: {component_type}')

    _save_prefab_changes(go, file_path)

    # Return the completed GameObject instance
    return go


def _save_prefab_changes(prefab: GameObject, prefab_file_path):
    # Load the JSON file into a dictionary
    with open(prefab_file_path, 'r') as f:
        json_data = json.load(f)

    # Modify the position of the Transform Component's position
    # This is in case we change the initial_position
    json_data['components'][0]['position'] = [prefab.initial_position.x, prefab.initial_position.y]

    # Write the updated data back to the JSON file
    with open(prefab_file_path, 'w') as f:
        json.dump(json_data, f, indent=4)


def _serialize_gameobject(go: GameObject, go_name):
    components_dict = [c.serialize() for c in go.components]
    return \
        {
            'gameobject_name': go_name,
            'initial_position': {'x': go.initial_position.x, 'y': go.initial_position.y},
            'image_path': go.image_path,
            'components': components_dict
        }
