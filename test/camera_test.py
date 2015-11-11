import cv2
def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    cap = cv2.VideoCapture(0)

    freq = 1000/cv2.getTickFrequency()
    start_time = cv2.getTickCount()
    oldcnt = 0
    cnt = 0
    while True:
        now_time  = cv2.getTickCount()
        diff_time = (now_time - start_time)*freq
        if diff_time > 1000:
            start_time = now_time
            fps = cnt - oldcnt
            oldcnt = cnt
            print fps

        ret, frame = cap.read()

        if mirror is True:
            frame = frame[:,::-1]

        if size is not None and len(size) == 2:
            frame = cv2.resize(frame, size)

        cv2.imshow('camera capture', frame)

        k = cv2.waitKey(1)
        if k == 27:
            break
        cnt += 1

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    capture_camera()
