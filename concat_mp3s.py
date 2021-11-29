import sys
from pydub import AudioSegment

def main():
	print("starting")
	file_path = sys.argv[1]
	file_count = int(sys.argv[2])

	output_sound = None
	for i in range(file_count):
		file_to_read = file_path + "-" + str(i) + ".mp3"
		print("reading file " + file_to_read)
		sound = AudioSegment.from_mp3(file_to_read)
		if (i == 0):
			output_sound = sound
		else:
			output_sound += sound

	output_sound.export(file_path + ".mp3", format="mp3")

if __name__ == "__main__":
    main()
