#version 150

// Makes blocks wobbly
vec3 wobble_position(vec3 position, float wobble_strength, float calmness, float gametime) {
     vec3 pos = position;

    float animX = (gametime * 2000 + pos.y + pos.z);
    float animY = (gametime * 3000 + pos.x + pos.z);
    float animZ = (gametime * 2500 + pos.x + pos.y);

    pos.x += sin(animX / calmness) / wobble_strength;
    pos.y += sin(animY / calmness) / wobble_strength;
    pos.z += sin(animZ / calmness) / wobble_strength;

    return pos;
}