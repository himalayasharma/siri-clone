import wave

obj = wave.open("data/experimental/StarWars3.wav", 'rb')

# Print specific params
print("Number of frames:", obj.getnframes())
print("Number of channels:", obj.getnchannels())
print("Frame rate:", obj.getframerate())
print("Duration of audio clip:", obj.getnframes()/obj.getframerate())
print("Sample width:", obj.getsampwidth())

# Print all params
print("All params:", obj.getparams())

# WORK WITH AUDIO
# Read all frames of audio
frames = obj.readframes(-1)
print("Type of frames object:", {type(frames)})
print("Length of frames object:", len(frames))
# Note: Length of frames object = sample width*number of frames
# Close object
obj.close()

# SAVE MODIFIED AUDIO AFTER WORKING
new_obj = wave.open("data/experimental/StarWars3Mod.wav", 'wb')
new_obj.setnchannels(1)
new_obj.setsampwidth(2)
new_obj.setframerate(22050)
new_obj.writeframes(frames)
# Close object
new_obj.close()



