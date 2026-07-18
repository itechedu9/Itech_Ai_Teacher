current_frame = None


def show(frame_creator, parent):

    global current_frame

    if current_frame is not None:
        current_frame.destroy()

    current_frame = frame_creator(parent)
