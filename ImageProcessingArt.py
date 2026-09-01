import sys #included in python
import cv2 #pip install opencv-python (needed for image input+output and convolutions)
import numpy as np #pip install numpy (sometimes included with python)
from matplotlib import pyplot as plt # pip install matplotlib

#Use the ImageDiff.py script to check your outputs against the correct outputs if unsure.
#if they are 100% or nearly 99.6+% correct your probably fine.

def Monkey():
    #Separate out the RGB channels of the monkey image
    #Different image libraries store image data differently
    #How does openCV store image data?
    #HINT check the origional image, what parts of the image are the most red, the most blue, the most green
    #     and how would that show up in the final images?
    monkey_image = cv2.imread("monkey.png")
    assert monkey_image is not None, "file could not be read"
    h, w, c = monkey_image.shape #height, width, color
    red_monkey = np.zeros(shape=(h, w, c), dtype=np.uint8) #make 3 placeholders ("empty" images)
    green_monkey = np.zeros(shape=(h, w, c), dtype=np.uint8)
    blue_monkey = np.zeros(shape=(h, w, c), dtype=np.uint8)
    ########################################YOUR CODE HERE########################################

    blue_monkey[:,:,0] = monkey_image[:,:,0]
    green_monkey[:,:,1] = monkey_image[:,:,1]
    red_monkey[:,:,2] = monkey_image[:,:,2]

    #note to self for future reference, 0 is B, 1 is G, 2 is R
    #so it aint RGB, its BGR. LMAO

    ##############################################################################################
    #write all 3 colors to new images (by default it is 3 black images)
    cv2.imwrite("monkeyred.png",red_monkey)
    cv2.imwrite("monkeygreen.png",green_monkey)
    cv2.imwrite("monkeyblue.png",blue_monkey)
    return

def Elk():
    #The elk picture is very low-contrast.
    #we want to raise the contrast to make the color "pop" a bit more.
    #take the image and multiply the color values to spread them out. (the expected output is 40% higher contrast)
    #then take those values and darken them so they dont go above the maximum brighness. 
    #HINT: what is the maximum value for a pixel normally? what is the maximum possible value after the multiplication?
    #HINT: this contrast function is the same as running the pixel colors through a linear equation. (ess. y = mx + b)
    elk_image = cv2.imread("elk.jpg")
    assert elk_image is not None, "file could not be read"
    h,w,c = elk_image.shape
    contrast_elk = np.zeros(shape=(h,w,c))
    ########################################YOUR CODE HERE########################################


    #the tolerance given is around 5% as the prof says, but lets see if we can get it as close as possible

    contrast_elk = elk_image * 1.4 - 102
    contrast_elk = np.clip(contrast_elk, 0, 255).astype(np.uint8)



    ##############################################################################################
    cv2.imwrite("contrastelk.jpg",contrast_elk)
    return

def Gamma():
    #We want to gamma-correct this image from wikipedia so that it is brighter
    #In real graphics applications this is done to better match human eye brightness sensitivity
    #It is also used to adjust for darker displays
    float_image = cv2.imread("float.png",0)
    assert float_image is not None, "file could not be read"
    h,w = float_image.shape
    gamma_float = np.zeros(shape=(h, w), dtype=np.uint8)
    #Use a gamma value of 0.5 to correct the image (assume a constant 1 scaling factor)
    ########################################YOUR CODE HERE########################################

    normalized = float_image / 255.0
    corrected = np.power(normalized, 0.5)
    gamma_float = np.clip(corrected * 255.0, 0, 255).astype(np.uint8)
    
    ##############################################################################################
    cv2.imwrite("gammafloat.jpg",gamma_float)
    return

def Lincoln():
    #blur pic of lincoln to obscure scratches in photograph
    #hint: kernel elements should sum to 1 for the entire kernel
    lincoln_image = cv2.imread("lincoln.jpg",0)
    assert lincoln_image is not None, "file could not be read"
    #kernel for average blur. Each pixel should be the average of its own 5x5 neighborhood.
    ########################################YOUR CODE HERE########################################
    avgkernel = np.ones((5, 5), dtype=np.float64) / 25.0
    ##############################################################################################
    #kernel for gaussian blur (hint: should be rougly identical to cv2.GaussianBlur(img,(5,5),0))
    #reccomend calculating using python/a calculator but the final result should use hard-coded numbers
    #hint: (only need to calculate 6 numbers due to symmetry) https://en.wikipedia.org/wiki/Gaussian_function
    ########################################YOUR CODE HERE########################################
    gausskernel = np.array([[ 0.005006,  0.017298,  0.026161,  0.017298,  0.005006 ],
       [ 0.017298, 0.059770, 0.090369, 0.059770,  0.017298],
       [ 0.026161, 0.090369, 0.136646 , 0.090369,  0.026161],
       [ 0.017298, 0.059770, 0.090369, 0.059770,  0.017298],
       [ 0.005006 ,  0.017298,  0.026161,  0.017298,  0.005006]])
    ##############################################################################################
    lincoln_avg = cv2.filter2D(src=lincoln_image, ddepth=-1, kernel=avgkernel) #apply kernels
    lincoln_gauss = cv2.filter2D(src=lincoln_image, ddepth=-1, kernel=gausskernel)

    cv2.imwrite("lincavg.jpg",lincoln_avg)
    cv2.imwrite("lincgauss.jpg",lincoln_gauss)
    return

def Astro():
    #This test case is OPTIONAL and replaces another test case if you get it right.
    #primitive edge detection on Eileen Collins NASA pic.
    #we will be performing sobel filetering for edge detection.
    #Wikipedia is helpfull here
    astro_image = cv2.imread("astro.jpg",0)
    h,w = astro_image.shape
    assert astro_image is not None, "file could not be read"

    #should make strong horizontal lines show in image and everything else black
    #hint: an edge is just a place where things change from one thing to another
    #hint (cont): horizontal lines divide something into top and bottom
    ########################################YOUR CODE HERE########################################

    #optional? Try me beyonce

    horizontalkernel = np.array([[-1.0,-2.0,-1.0],
                            [0.0,0.0,0.0],
                            [1.0,2.0,1.0]])
    ##############################################################################################
    #should make strong vertical lines show in image and everything else black
    #hint: vertical lines divide something into left and right
    ########################################YOUR CODE HERE########################################
    verticalkernel = np.array([[-1.0,0.0,1.0],
                            [-2.0,0.0,2.0],
                            [-1.0,0.0,1.0]])
    ##############################################################################################
    astro_horizontal = cv2.filter2D(src=astro_image, ddepth=-1, kernel=horizontalkernel) #apply kernels
    astro_vertical = cv2.filter2D(src=astro_image, ddepth=-1, kernel=verticalkernel)

    astro_edge = np.zeros(shape=(h, w), dtype=np.uint8)
    #should show all edges.
    #hint: should be easy if the first two are correct (no additional kernels needed)
    #there are several ways to combine this, dont worry if your results dont match mine, as long as it looks close you get full credit
    ########################################YOUR CODE HERE########################################
    astro_edge = cv2.add(astro_horizontal, astro_vertical)
    ##############################################################################################

    cv2.imwrite("astrohorizontal.jpg",astro_horizontal)
    cv2.imwrite("astrovertical.jpg",astro_vertical)
    cv2.imwrite("astroedge.jpg",astro_edge)
    return

def Signature():
    #using an image of a Handwritten Signature, use Image Thresholding to make a Black and White image of the signature

    signature_image = cv2.imread("JohnDoe.jpg", 0)
    assert signature_image is not None, "file could not be read"
    signature_copy = signature_image.copy()
    h, w = signature_image.shape #height, width
    sig_thresh = np.zeros(shape=(h, w), dtype=np.uint8) #make 2 placeholders
    sig_gaussthresh = np.zeros(shape=(h, w), dtype=np.uint8)

    #blur the copy image 50 times using the kernel from Lincoln
    #we could use a bigger kernel with better thresholding but brute force will work for our purposes
    ########################################YOUR CODE HERE########################################
    gausskernel = np.array([[ 0.005006,  0.017298,  0.026161,  0.017298,  0.005006 ],
       [ 0.017298, 0.059770, 0.090369, 0.059770,  0.017298],
       [ 0.026161, 0.090369, 0.136646 , 0.090369,  0.026161],
       [ 0.017298, 0.059770, 0.090369, 0.059770,  0.017298],
       [ 0.005006 , 0.017298, 0.026161, 0.017298, 0.005006]])
    #something more here

    for _ in range(50):
        signature_copy = cv2.filter2D(src=signature_copy, ddepth=-1, kernel=gausskernel)

    #python syntax gives me an aneurysm

    ##############################################################################################

    #each pixel should be black(0) if part of the signature and white(255) otherwise. threshold at 100 out of 255.
    #do this with 2 for loops, NOT the threshold funciton built into opencv
    #hint: the paper is white-ish but the signature is pencil and is closer to black.
    ########################################YOUR CODE HERE########################################
    for i in range(h):
        for j in range(w):
            sig_thresh[i][j] = 0 if signature_image[i][j] < 100 else 255
            sig_gaussthresh[i][j] = 0 if signature_copy[i][j] < 100 else 255
    #eughhhhh, brotha euuuuuuughhhhh

    ##############################################################################################
    cv2.imwrite("SigThresh.png", sig_thresh) #get this one working correctly first!
    cv2.imwrite("SigBlurThresh.png", sig_gaussthresh)
    return

def Art():
    #using any image labled "custom.png" in the same directory/folder as this script
    #use a combination of filters (and any additional manipulations you find interesting) to make a cool image.
    #Art sumbissions should be unique for each student, come up with something weird.
    art_image = cv2.imread("custom.png") #swap astro.jpg with custom.png when you are ready.
    assert art_image is not None, "file could not be read"
    ########################################YOUR CODE HERE########################################
    
    # BRAVO SIX, GOING DARK
    # This is a night vision-style image manipulation. 
    # it combines everything this assignment tests and a few other techniques I've heard of.
    h, w, c = art_image.shape
    gray = cv2.cvtColor(art_image, cv2.COLOR_BGR2GRAY)
    #night vis brightens up whatever you see, so I used CLAHE to up contrast
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    equalized = clahe.apply(gray)

    #gamma up for more brightness
    gamma = 0.45
    normalized = equalized.astype(np.float64) / 255.0
    brightened = np.power(normalized, gamma) * 255.0
    brightened = np.clip(brightened, 0, 255).astype(np.uint8)

    #we use gaussian blur to make a grain style effect 
    noise = np.random.normal(0, 10, brightened.shape).astype(np.float64)
    noisy = np.clip(brightened.astype(np.float64) + noise, 0, 255).astype(np.uint8)
    noisy = cv2.GaussianBlur(noisy, (3, 3), 0)

    # monochrome green
    nightvision = np.zeros((h, w, 3), dtype=np.uint8)
    nightvision[:, :, 1] = noisy
    nightvision[:, :, 0] = (noisy.astype(np.float64) * 0.05).astype(np.uint8)
    nightvision[:, :, 2] = (noisy.astype(np.float64) * 0.12).astype(np.uint8)

    #scanlines for an analog style, done via clever array slicing and multiplication
    scanline_mask = np.ones((h, 1), dtype=np.float64)
    scanline_mask[::2] = 0.78
    nightvision = (nightvision.astype(np.float64) * scanline_mask[:, :, None]).astype(np.uint8)

    


    art_image = nightvision

    ##############################################################################################
    cv2.imwrite("art.jpg",art_image)
    return

if __name__ == "__main__":
    #avoid making changes to this
    if len(sys.argv) > 1:
        if sys.argv[1] == "lincoln":
            Lincoln()
        elif sys.argv[1] == "astro":
            Astro()
        elif sys.argv[1] == "contrast":
            Elk()
        elif sys.argv[1] == "gamma":
            Gamma()
        elif sys.argv[1] == "monkey":
            Monkey()
        elif sys.argv[1] == "signature":
            Signature()
        elif sys.argv[1] == "art":
            Art()
    else:
        print("missing/impropper arguements: usage \"python ImageProcessingArt.py <lincoln/contrast/gamma/astro/monkey/signature/art>\"")