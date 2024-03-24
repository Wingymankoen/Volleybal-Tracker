import cv2 as cv


def get_high(mask):
    cnts, _ = cv.findContours(mask, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)
    chigh = None
    cy = 10000
    for c in cnts:
        x, y, w, h = cv.boundingRect(c)
        s = min(w, h)
        if s < 15:
            continue

        if y < cy:
            r = max(w, h) / s
            if r > 1.5:
                continue

            cy = y
            chigh = c
    return chigh


def get_ball(figs, wd):

    for idx, frame in enumerate(figs):
        mask = cv.GaussianBlur(frame, (7, 7), 0)
        mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
        ret, mask = cv.threshold(mask, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
        chigh = get_high(mask)
        if chigh is not None:
            rx, ry, rw, rh = cv.boundingRect(chigh)
            #mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
            cut = mask[ry: ry + rh, rx: rx + rw]
            cv.imwrite(wd + '\\Data\\Contours' + "\\cleared%d.jpg" % idx, cut)

        #cv.imwrite(wd + "\\temp.jpg", mask)
