import numpy as np
from sagittal_average.sagittal_brain import run_averages
#import subprocess
from pathlib import Path

TEST_DIR = Path(__file__).parent

def test_average():
    data_input = np.zeros((20, 20))
    data_input[-1, :] = 1
    np.savetxt(TEST_DIR / "brain_sample.csv", data_input, fmt='%d', delimiter=',')

    #subprocess.run(["python", "sagittal_brain.py"])

    expected = np.zeros(20)
    expected[-1] = 1

    #run python program
    run_averages(file_input=TEST_DIR / "brain_sample.csv", file_output=TEST_DIR / "brain_average.csv")
    output = np.loadtxt(TEST_DIR / "brain_average.csv", delimiter=',')

    #output = np.loadtxt("brain_average.csv", delimiter=",")

    assert np.array_equal(expected, output)