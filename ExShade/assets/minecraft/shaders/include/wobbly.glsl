#version 150

// Makes blocks wobbly
vec3 wobble_position(vec3 position, float gametime) {
    float wobble_strength = 0.5;
    float calmness = 4;
    vec3 pos = position;

    float animX = (gametime * 3000 + pos.y + pos.z);
    float animY = (gametime * 2500 + pos.x + pos.z);
    float animZ = (gametime * 2000 + pos.x + pos.y);

    pos.x += sin(animX / calmness) * wobble_strength;
    pos.y += cos(animY / calmness) * wobble_strength;
    pos.z += sin(animZ / calmness) * wobble_strength;

    return pos;
}