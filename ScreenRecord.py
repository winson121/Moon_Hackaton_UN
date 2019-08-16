def screenRecord(title='window'):
    start_time = time.time()
    while (True):
        printscreen = np.array(ImageGrab.grab(bbox=(0,40,800,640)))
        print('eta: {}'.format(time.time()-start_time))
        cv2.imshow(title, cv2.cvtColor(printscreen,cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break