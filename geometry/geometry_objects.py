"""Module with additional objects to help with geometry creation

These are based on the noodle_objects.py module and impliment validation
"""


from typing import Optional

import rigatoni

class AttributeInput(rigatoni.NoodleObject):
    """Input for setting attributes of a buffer 
    
    User should not have to concern themselves with this input
    """

    semantic: rigatoni.AttributeSemantic
    format: rigatoni.Format
    normalized: bool
    offset: rigatoni.Optional[int]
    stride: rigatoni.Optional[int]


class GeometryPatchInput(rigatoni.NoodleObject):
    """User input object for creating a geometry patch"""

    vertices: list
    indices: list
    index_type: str 
    material: rigatoni.MaterialID
    normals: Optional[list] 
    tangents: Optional[list]
    textures:Optional[list] 
    colors: Optional[list]


