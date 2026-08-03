import librosa
import numpy as np
import matplotlib.pyplot as plt

def plot_wave(data_h,data_p,sr):

    fig,ax = plt.subplots(1,2,figsize = (12,6))

     
    librosa.display.waveshow(data_h,sr=sr,ax=ax[0])
    ax[0].set_title("Harmonic component")
    ax[0].set_xlabel("Time")
    ax[0].set_ylabel("Amplitude")  

    librosa.display.waveshow(data_p,sr=sr,ax=ax[1])
    ax[1].set_title("Percussive component")
    ax[1].set_xlabel("Time")
    ax[1].set_ylabel("Amplitude") 

    plt.tight_layout()
    plt.show()

    return None

def plot_melspectrogram(data_h,data_p,sr):

    spect_h = librosa.feature.melspectrogram(y=data_h, sr = sr,n_mels = 128)
    spect_p = librosa.feature.melspectrogram(y=data_p, sr = sr,n_mels = 128)

    #convert to decibels(dB)
    spect_h_db = librosa.power_to_db(spect_h,ref = np.max) 
    spect_p_db = librosa.power_to_db(spect_p,ref = np.max) 

    fig,ax = plt.subplots(1,2,figsize = (20,6))

     
    librosa.display.specshow(spect_h_db,sr = sr,x_axis="time",y_axis ="mel",ax = ax[0])
    ax[0].set_title("Harmonic component")  

    img_p = librosa.display.specshow(spect_p_db,sr = sr,x_axis="time",y_axis ="mel",ax = ax[1])
    ax[1].set_title("Percussive component")

    fig.colorbar(img_p,ax =ax,location = "right",format='%+2.0f dB')
   
    plt.show()

    return None


def HPSS(path):
    '''Harmonic-Percussive Source Separation (HPSS)'''

    data,sr = librosa.load(path)
    data_h,data_p = librosa.effects.hpss(data)

    plot_wave(data_h,data_p,sr)
    plot_melspectrogram(data_h,data_p,sr)

    return data,data_h,data_p,sr


if __name__ == "__main__":

    file_path = r"E:\infotact\project_as\AcousticSpace\dataset\sample\0_george_14.wav"
    audio_data,data_harmonic,data_percussive,sample_rate = HPSS(file_path)



    
