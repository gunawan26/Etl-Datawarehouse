def new_w(w, aw):
    w = w+aw
    return w


def new_b(b, ab):
    b = b+ab
    return b


def delta_w(alpha, t, y, x):
    aw = alpha(t-y)*x
    return aw


def delta_b(alpha, t, y):
    ab = alpha(t-y)*t
    return ab


def f_net(b, x1, w1, x2, w2):
    net = b+((x1*w1)+(x2*w2))
    return net


def f_epoch():
    alpha = 0.1
    maxw = 1.1
    w1 = 0
    w2 = 0
    b = 0
    x1 = [1, 1, -1, -1]
    x2 = [1, -1, 1, -1]
    t = [1, -1, -1, -1]
    i = 0
    epoch = 1
    while maxw > 0.07:
        if i > 3:
            i = 0
        print("=============================== EPOCH %d ===============================" %epoch)
        y = f_net(b, x1[i], x2[i], w1, w2)
        print("Nilai Net = %f" %y)
        aw1 = delta_w(alpha, t[i], y, x1[i])
        print("Nilai Aw1 = %f" % aw1)
        aw2 = delta_w(alpha, t[i], y, x2[i])
        print("Nilai Aw2 = %f" % aw2)
        ab = delta_b(alpha, t[i], y)
        print("Nilai Ab = %f" % ab)
        w1 = new_w(w1, aw1)
        print("Nilai w1 baru = %f" % w1)
        w2 = new_w(w2, aw2)
        print("Nilai w2 baru = %f" % w2)
        b = new_b(b, ab)
        print("Nilai b baru = %f" % b)
        if aw1 > aw2:
            maxw = aw1
        else:
            maxw = aw2
        i = i+1
        epoch = epoch+1



f_epoch()