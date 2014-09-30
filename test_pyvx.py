from pyvx.backend import *
from array import array

class TestPyVx(object):
    def test_gaussian(self):
        g = Graph()
        with g:
            img = Image(3, 4, FOURCC_U8, array('B', range(12)))
            gimg = Gaussian3x3(img)
            gimg.force()
        g.verify()
        g.process()
        assert gimg.data[4] == 4
        assert gimg.data[7] == 7

    def test_replicate_border(self):
        g = Graph()
        with g:
            img = Image(3, 4, FOURCC_U8, array('B', range(12)))
            gimg = Gaussian3x3(img)
            gimg.producer.border_mode = BORDER_MODE_REPLICATE
            gimg.force()
        g.verify()
        g.process()
        assert gimg.data[0] == 1
        assert gimg.data[1] == 1
        assert gimg.data[11] == 10

    def test_add(self):
        g = Graph()
        with g:
            img = Image(3, 4, FOURCC_U8, array('B', range(12)))
            sa = img + img
            sa.force()
        g.verify()
        g.process()
        for i in range(12):
            assert sa.data[i] == 2*i

    def test_channel_extract_rgb(self):
        g = Graph()
        with g:
            img = Image(3, 4, FOURCC_RGB, array('B', range(12*3)))
            rimg = img.channel_r
            rimg.force()
            gimg = img.channel_g
            gimg.force()
            bimg = img.channel_b
            bimg.force()
        g.verify()
        g.process()
        for i in range(12):
            assert rimg.data[i] == 3*i
            assert gimg.data[i] == 3*i + 1
            assert bimg.data[i] == 3*i + 2

    def test_channel_extract_uyvu(self):
        g = Graph()
        with g:
            img = Image(3, 4, FOURCC_UYVY, array('B', range(12*2)))
            yimg = img.channel_y
            yimg.force()
            uimg = img.channel_u
            uimg.force()
            vimg = img.channel_v
            vimg.force()
        g.verify()
        g.process()
        assert [yimg.data[i] for i in range(7)] == [1,3,5,7,9,11,13]
        assert [uimg.data[i] for i in range(7)] == [0,0,4,4,8,8,12]
        assert [vimg.data[i] for i in range(7)] == [2,2,6,6,10,10,14]