#version 150

#moj_import <light.glsl>
#moj_import <fog.glsl>
#moj_import <wobbly.glsl>

in vec3 Position;
in vec4 Color;
in vec2 UV0;
in ivec2 UV2;
in vec3 Normal;

uniform sampler2D Sampler2;

uniform mat4 ModelViewMat;
uniform mat4 ProjMat;
uniform vec3 ChunkOffset;
uniform int FogShape;
uniform float GameTime;

out float vertexDistance;
out vec4 vertexColor;
out vec2 texCoord0;
out vec4 normal;

void main() {
    vec3 pos = Position + ChunkOffset;
    pos = wobble_position(pos, GameTime);

    gl_Position = ProjMat * ModelViewMat * vec4(pos, 1.0);

    vertexDistance = fog_distance(ModelViewMat, pos, FogShape);
    vertexColor = Color * minecraft_sample_lightmap(Sampler2, UV2);
    vec2 uv = UV0;
    uv.y+=sin(GameTime * 10)/2+0.5;

    texCoord0 = uv;

    normal = ProjMat * ModelViewMat * vec4(Normal, 0.0);
}

