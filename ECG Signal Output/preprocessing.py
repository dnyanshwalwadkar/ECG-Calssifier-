import heartpy as hp

data = hp.get_data('D:\\mass technologies\\project 2017-18\\Jay Kanewar\\100.csv',column_name='MLII')
working_data, measures = hp.process(data, 300.0)
hp.plotter(working_data, measures,title="RAW ECG SIGNAL")


import numpy as np
# import heartpy as hp

# from scipy.signal import butter, filtfilt, iirnotch, savgol_filter

# data = hp.get_data('D:\\mass technologies\\project 2017-18\\Jay Kanewar\\MRDataset102.csv')

filteredlowpass = hp.filtering.filter_signal(data, cutoff = 60, sample_rate = 300.0, order = 3,filtertype='lowpass')
working_data,measures=hp.process(filteredlowpass,300.0)
# print(np.around(filtered[0:6], 3))
hp.plotter(working_data, measures)

# filteredhighpass = hp.filtering.filter_signal(data, cutoff = 0.75, sample_rate = 100.0, order = 3,filtertype='highpass')
# working_data1,measures1=hp.process(filteredhighpass,100.0)
# hp.plotter(working_data1, measures1)

# filtered = hp.butter_lowpass_filter(data, cutoff=5, sample_rate=100.0, order=3)

# # from scipy import signal
# # import matplotlib.pyplot as plt

# # b, a = signal.butter(4, data, 'low', analog=True)

# # w, h = signal.freqs(b, a)
# # plt.plot(w, 20 * np.log10(abs(h)))
# # plt.xscale('log')
# # plt.title('Butterworth filter frequency response')
# # plt.xlabel('Frequency [radians / second]')
# # plt.ylabel('Amplitude [dB]')
# # plt.margins(0, 0.1)
# # plt.grid(which='both', axis='both')
# # plt.axvline(100, color='green') # cutoff frequency
# # plt.show()


# # filtered = hp.butter_lowpass_filter(data, cutoff=5, sample_rate=100.0, order=3)
# # working_data2,measures2=hp.process(filteredbutterworth,100.0)

# # hp.plotter(working_data2,measures2)


