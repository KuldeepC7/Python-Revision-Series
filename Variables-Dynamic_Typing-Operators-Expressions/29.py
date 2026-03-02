# 29. A low-level audio processing algorithm handles values as integers. Use the bitwise NOT (~) and addition to calculate the two's complement (mathematical negation) of an audio sample value sample = 45, mimicking how system architectures handle negative numbers.

# ~2 = -(2+1) = -3

sample = 45
negative_sample = ~sample + 1
print(negative_sample)