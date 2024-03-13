import cv2 as cv


def get_high(mask):
    cnts, _ = cv.findContours(mask, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)


def get_ball(figs, wd):

    for frame in figs:
        mask = cv.GaussianBlur(frame, (7, 7), 0)
        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        ret, mask = cv.threshold(mask, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        #cmask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
        chigh = get_high(mask)

        #cv.imwrite(wd + "\\temp.jpg", mask)



