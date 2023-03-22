import numpy as np
import tkinter as tk
import pytest

from video_vocal_rt import experiment

@pytest.fixture
def mocked_tk(mocker):
    mocked_root = mocker.MagicMock(spec=tk.Tk)
    mocked_root.winfo_screenheight.return_value = 1080
    mocked_root.winfo_screenwidth.return_value = 1920
    mocker.patch('video_vocal_rt.experiment.tk.Tk', return_value=mocked_root)
    return mocked_root

def test_create_white_screen(mocked_tk):
    white_screen = experiment.create_white_screen()
    assert isinstance(white_screen, np.ndarray)
    assert white_screen.shape == (1080, 1920, 3)
    assert np.all(white_screen == 255)

def test_get_center_coordinates(mocked_tk):
    image = experiment.create_white_screen()
    center = experiment.get_center_coordinates(image)
    assert center == (960, 540)

def test_create_fixation_screen(mocked_tk):
    fixation_screen = experiment.create_fixation_screen()
    assert isinstance(fixation_screen, np.ndarray)
    assert fixation_screen.shape == (1080, 1920, 3)
