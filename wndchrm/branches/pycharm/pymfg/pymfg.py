# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.4
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pymfg', [dirname(__file__)])
        except ImportError:
            import _pymfg
            return _pymfg
        if fp is not None:
            try:
                _mod = imp.load_module('_pymfg', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pymfg = swig_import_helper()
    del swig_import_helper
else:
    import _pymfg
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class RGBcolor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, RGBcolor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, RGBcolor, name)
    __repr__ = _swig_repr
    __swig_setmethods__["red"] = _pymfg.RGBcolor_red_set
    __swig_getmethods__["red"] = _pymfg.RGBcolor_red_get
    if _newclass:red = _swig_property(_pymfg.RGBcolor_red_get, _pymfg.RGBcolor_red_set)
    __swig_setmethods__["green"] = _pymfg.RGBcolor_green_set
    __swig_getmethods__["green"] = _pymfg.RGBcolor_green_get
    if _newclass:green = _swig_property(_pymfg.RGBcolor_green_get, _pymfg.RGBcolor_green_set)
    __swig_setmethods__["blue"] = _pymfg.RGBcolor_blue_set
    __swig_getmethods__["blue"] = _pymfg.RGBcolor_blue_get
    if _newclass:blue = _swig_property(_pymfg.RGBcolor_blue_get, _pymfg.RGBcolor_blue_set)
    def __init__(self): 
        this = _pymfg.new_RGBcolor()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pymfg.delete_RGBcolor
    __del__ = lambda self : None;
RGBcolor_swigregister = _pymfg.RGBcolor_swigregister
RGBcolor_swigregister(RGBcolor)

class HSVcolor(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, HSVcolor, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, HSVcolor, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hue"] = _pymfg.HSVcolor_hue_set
    __swig_getmethods__["hue"] = _pymfg.HSVcolor_hue_get
    if _newclass:hue = _swig_property(_pymfg.HSVcolor_hue_get, _pymfg.HSVcolor_hue_set)
    __swig_setmethods__["saturation"] = _pymfg.HSVcolor_saturation_set
    __swig_getmethods__["saturation"] = _pymfg.HSVcolor_saturation_get
    if _newclass:saturation = _swig_property(_pymfg.HSVcolor_saturation_get, _pymfg.HSVcolor_saturation_set)
    __swig_setmethods__["value"] = _pymfg.HSVcolor_value_set
    __swig_getmethods__["value"] = _pymfg.HSVcolor_value_get
    if _newclass:value = _swig_property(_pymfg.HSVcolor_value_get, _pymfg.HSVcolor_value_set)
    def __init__(self): 
        this = _pymfg.new_HSVcolor()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pymfg.delete_HSVcolor
    __del__ = lambda self : None;
HSVcolor_swigregister = _pymfg.HSVcolor_swigregister
HSVcolor_swigregister(HSVcolor)

class color(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, color, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, color, name)
    __repr__ = _swig_repr
    __swig_setmethods__["RGB"] = _pymfg.color_RGB_set
    __swig_getmethods__["RGB"] = _pymfg.color_RGB_get
    if _newclass:RGB = _swig_property(_pymfg.color_RGB_get, _pymfg.color_RGB_set)
    __swig_setmethods__["HSV"] = _pymfg.color_HSV_set
    __swig_getmethods__["HSV"] = _pymfg.color_HSV_get
    if _newclass:HSV = _swig_property(_pymfg.color_HSV_get, _pymfg.color_HSV_set)
    def __init__(self): 
        this = _pymfg.new_color()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pymfg.delete_color
    __del__ = lambda self : None;
color_swigregister = _pymfg.color_swigregister
color_swigregister(color)

class pix_data(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pix_data, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pix_data, name)
    __repr__ = _swig_repr
    __swig_setmethods__["clr"] = _pymfg.pix_data_clr_set
    __swig_getmethods__["clr"] = _pymfg.pix_data_clr_get
    if _newclass:clr = _swig_property(_pymfg.pix_data_clr_get, _pymfg.pix_data_clr_set)
    __swig_setmethods__["intensity"] = _pymfg.pix_data_intensity_set
    __swig_getmethods__["intensity"] = _pymfg.pix_data_intensity_get
    if _newclass:intensity = _swig_property(_pymfg.pix_data_intensity_get, _pymfg.pix_data_intensity_set)
    def __init__(self): 
        this = _pymfg.new_pix_data()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pymfg.delete_pix_data
    __del__ = lambda self : None;
pix_data_swigregister = _pymfg.pix_data_swigregister
pix_data_swigregister(pix_data)

class rect(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, rect, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, rect, name)
    __repr__ = _swig_repr
    __swig_setmethods__["x"] = _pymfg.rect_x_set
    __swig_getmethods__["x"] = _pymfg.rect_x_get
    if _newclass:x = _swig_property(_pymfg.rect_x_get, _pymfg.rect_x_set)
    __swig_setmethods__["y"] = _pymfg.rect_y_set
    __swig_getmethods__["y"] = _pymfg.rect_y_get
    if _newclass:y = _swig_property(_pymfg.rect_y_get, _pymfg.rect_y_set)
    __swig_setmethods__["w"] = _pymfg.rect_w_set
    __swig_getmethods__["w"] = _pymfg.rect_w_get
    if _newclass:w = _swig_property(_pymfg.rect_w_get, _pymfg.rect_w_set)
    __swig_setmethods__["h"] = _pymfg.rect_h_set
    __swig_getmethods__["h"] = _pymfg.rect_h_get
    if _newclass:h = _swig_property(_pymfg.rect_h_get, _pymfg.rect_h_set)
    def __init__(self): 
        this = _pymfg.new_rect()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pymfg.delete_rect
    __del__ = lambda self : None;
rect_swigregister = _pymfg.rect_swigregister
rect_swigregister(rect)


def compare_doubles(*args):
  return _pymfg.compare_doubles(*args)
compare_doubles = _pymfg.compare_doubles
class ImageMatrix(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ImageMatrix, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ImageMatrix, name)
    __repr__ = _swig_repr
    __swig_setmethods__["data"] = _pymfg.ImageMatrix_data_set
    __swig_getmethods__["data"] = _pymfg.ImageMatrix_data_get
    if _newclass:data = _swig_property(_pymfg.ImageMatrix_data_get, _pymfg.ImageMatrix_data_set)
    __swig_setmethods__["ColorMode"] = _pymfg.ImageMatrix_ColorMode_set
    __swig_getmethods__["ColorMode"] = _pymfg.ImageMatrix_ColorMode_get
    if _newclass:ColorMode = _swig_property(_pymfg.ImageMatrix_ColorMode_get, _pymfg.ImageMatrix_ColorMode_set)
    __swig_setmethods__["bits"] = _pymfg.ImageMatrix_bits_set
    __swig_getmethods__["bits"] = _pymfg.ImageMatrix_bits_get
    if _newclass:bits = _swig_property(_pymfg.ImageMatrix_bits_get, _pymfg.ImageMatrix_bits_set)
    __swig_setmethods__["width"] = _pymfg.ImageMatrix_width_set
    __swig_getmethods__["width"] = _pymfg.ImageMatrix_width_get
    if _newclass:width = _swig_property(_pymfg.ImageMatrix_width_get, _pymfg.ImageMatrix_width_set)
    __swig_setmethods__["height"] = _pymfg.ImageMatrix_height_set
    __swig_getmethods__["height"] = _pymfg.ImageMatrix_height_get
    if _newclass:height = _swig_property(_pymfg.ImageMatrix_height_get, _pymfg.ImageMatrix_height_set)
    __swig_setmethods__["depth"] = _pymfg.ImageMatrix_depth_set
    __swig_getmethods__["depth"] = _pymfg.ImageMatrix_depth_get
    if _newclass:depth = _swig_property(_pymfg.ImageMatrix_depth_get, _pymfg.ImageMatrix_depth_set)
    def LoadTIFF(self, *args): return _pymfg.ImageMatrix_LoadTIFF(self, *args)
    def SaveTiff(self, *args): return _pymfg.ImageMatrix_SaveTiff(self, *args)
    def LoadPPM(self, *args): return _pymfg.ImageMatrix_LoadPPM(self, *args)
    def OpenImage(self, *args): return _pymfg.ImageMatrix_OpenImage(self, *args)
    def __init__(self, *args): 
        this = _pymfg.new_ImageMatrix(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pymfg.delete_ImageMatrix
    __del__ = lambda self : None;
    def duplicate(self): return _pymfg.ImageMatrix_duplicate(self)
    def pixel(self, *args): return _pymfg.ImageMatrix_pixel(self, *args)
    def set(self, *args): return _pymfg.ImageMatrix_set(self, *args)
    def SetInt(self, *args): return _pymfg.ImageMatrix_SetInt(self, *args)
    def diff(self, *args): return _pymfg.ImageMatrix_diff(self, *args)
    def normalize(self, *args): return _pymfg.ImageMatrix_normalize(self, *args)
    def to8bits(self): return _pymfg.ImageMatrix_to8bits(self)
    def flip(self): return _pymfg.ImageMatrix_flip(self)
    def invert(self): return _pymfg.ImageMatrix_invert(self)
    def Downsample(self, *args): return _pymfg.ImageMatrix_Downsample(self, *args)
    def Rotate(self, *args): return _pymfg.ImageMatrix_Rotate(self, *args)
    def convolve(self, *args): return _pymfg.ImageMatrix_convolve(self, *args)
    def BasicStatistics(self, *args): return _pymfg.ImageMatrix_BasicStatistics(self, *args)
    def GetColorStatistics(self, *args): return _pymfg.ImageMatrix_GetColorStatistics(self, *args)
    def ColorTransform(self, *args): return _pymfg.ImageMatrix_ColorTransform(self, *args)
    def histogram(self, *args): return _pymfg.ImageMatrix_histogram(self, *args)
    def Otsu(self): return _pymfg.ImageMatrix_Otsu(self)
    def MultiScaleHistogram(self, *args): return _pymfg.ImageMatrix_MultiScaleHistogram(self, *args)
    def EdgeTransform(self): return _pymfg.ImageMatrix_EdgeTransform(self)
    def fft2(self): return _pymfg.ImageMatrix_fft2(self)
    def ChebyshevTransform(self, *args): return _pymfg.ImageMatrix_ChebyshevTransform(self, *args)
    def ChebyshevFourierTransform2D(self, *args): return _pymfg.ImageMatrix_ChebyshevFourierTransform2D(self, *args)
    def Symlet5Transform(self): return _pymfg.ImageMatrix_Symlet5Transform(self)
    def GradientMagnitude(self, *args): return _pymfg.ImageMatrix_GradientMagnitude(self, *args)
    def GradientDirection2D(self, *args): return _pymfg.ImageMatrix_GradientDirection2D(self, *args)
    def PerwittMagnitude2D(self, *args): return _pymfg.ImageMatrix_PerwittMagnitude2D(self, *args)
    def PerwittDirection2D(self, *args): return _pymfg.ImageMatrix_PerwittDirection2D(self, *args)
    def ChebyshevStatistics2D(self, *args): return _pymfg.ImageMatrix_ChebyshevStatistics2D(self, *args)
    def CombFirstFourMoments2D(self, *args): return _pymfg.ImageMatrix_CombFirstFourMoments2D(self, *args)
    def EdgeStatistics(self, *args): return _pymfg.ImageMatrix_EdgeStatistics(self, *args)
    def RadonTransform2D(self, *args): return _pymfg.ImageMatrix_RadonTransform2D(self, *args)
    def OtsuBinaryMaskTransform(self): return _pymfg.ImageMatrix_OtsuBinaryMaskTransform(self)
    def BWlabel(self, *args): return _pymfg.ImageMatrix_BWlabel(self, *args)
    def centroid(self, *args): return _pymfg.ImageMatrix_centroid(self, *args)
    def FeatureStatistics(self, *args): return _pymfg.ImageMatrix_FeatureStatistics(self, *args)
    def GaborFilters2D(self, *args): return _pymfg.ImageMatrix_GaborFilters2D(self, *args)
    def HaarlickTexture2D(self, *args): return _pymfg.ImageMatrix_HaarlickTexture2D(self, *args)
    def TamuraTexture2D(self, *args): return _pymfg.ImageMatrix_TamuraTexture2D(self, *args)
    def zernike2D(self, *args): return _pymfg.ImageMatrix_zernike2D(self, *args)
ImageMatrix_swigregister = _pymfg.ImageMatrix_swigregister
ImageMatrix_swigregister(ImageMatrix)


def RGB2HSV(*args):
  return _pymfg.RGB2HSV(*args)
RGB2HSV = _pymfg.RGB2HSV

def HSV2RGB(*args):
  return _pymfg.HSV2RGB(*args)
HSV2RGB = _pymfg.HSV2RGB

def RGB2COLOR(*args):
  return _pymfg.RGB2COLOR(*args)
RGB2COLOR = _pymfg.RGB2COLOR

def COLOR2GRAY(*args):
  return _pymfg.COLOR2GRAY(*args)
COLOR2GRAY = _pymfg.COLOR2GRAY
# This file is compatible with both classic and new-style classes.


