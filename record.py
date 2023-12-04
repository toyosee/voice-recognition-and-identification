import os
import pyaudio
import wave

def record_audio(duration=15):
    folder_name = 'recordings'
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Determine the next available filename by checking existing files in the 'recordings' folder
    existing_recordings = os.listdir(folder_name)
    existing_samples = [f for f in existing_recordings if f.startswith('sample')]
    last_sample_number = len(existing_samples)
    next_filename = f"sample{last_sample_number + 1}.wav"
    
    file_path = os.path.join(folder_name, next_filename)
    
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1  # Mono
    fs = 44100  # Record at 44.1 kHz sampling frequency
    seconds = duration
    
    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    
    # Check available audio devices and set the default input device
    default_device_index = p.get_default_input_device_info().get('index')
    device_info = p.get_device_info_by_index(default_device_index)
    
    if device_info['maxInputChannels'] == 0:
        print("No external microphone detected. Using default system microphone.")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True,
                    input_device_index=default_device_index)

    print("Recording...")
    frames = []  # Initialize array to store frames

    # Record for the specified duration
    for i in range(0, int(fs / chunk * seconds)):
        try:
            data = stream.read(chunk)
            frames.append(data)
        except Exception as e:
            print(f"Error recording: {e}")
            break

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print("Finished recording.")

    # Save the recorded data as a WAV file
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"Recording saved to '{file_path}'.")

# Record a new voice sample for 15 seconds and save it with an incremented filename in the 'recordings' folder
record_audio(duration=15)
