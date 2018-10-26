first of all, in this project, we try to implement 3 main filters and transformations in machine vision 
and an implementation of convolution  

the project contains 3 main packages: Basics, Filters, and Test

in the Basics Package, we have the imageIO class that give us the main methods to interact with the files and read images 
convert them to Matrix and converting Matrix to images, methods to visualization of the result by Java Swing and

the next class OPs contains some useful methods like basic convolution in n^2 * m^2 order and Matrix Functions

one of the questions in the project was reducing convolution order so :

## reducing Convolution order:

every iteration of convolution contains the summation of m^2-(2*m) last iteration so we can use the idea of rolling sum and save the last m^2-(2*m) productions and only compute the new 2*m rows 

in this case, the order reduces to n^2*(2*m) so it will be run in O(n^2*m)

![alt tag](https://github.com/AlirezaAzadbakht/Machine-Vision/blob/master/Filters/images/ConvolutionExpl.jpg
)

our Test Classes are simple

```Java
public static void main(String[] args) {
		imageIO i = new imageIO();		
		File file = new File("DIR");
		BufferedImage img;
		img = i.LoadImage(file);
		i.ShowImage(img);
		int[][] data = i.GetImageMatrix(img);
		
		data =  new SobelFilter(data).getResult();
		img = i.MatrixtoImage(data,1);
		i.ShowImage(img);

	}
```
all the filters have the .getResult() function so after calling the constructor we simply use the function and get the results

the result of our convolution implementation for our Benchmark image 

IMAGE.TEST

was 

ConvolutionIMAGE


## SOBEL FILTER

we simply follow as WIKIPEDIA https://en.wikipedia.org/wiki/Sobel_operator and implement the Steps

```Java
public SobelFilter(int imageMatrix[][]) {
		System.out.println("Sobel Filter Called.");
		this.imageMatrix = imageMatrix;
		Gx = OPs.convolution(imageMatrix, kernelMatrix1);
		Gy = OPs.convolution(imageMatrix, kernelMatrix2);
		ResultMatrix=OPs.mergeTwoMatrix(Gx, Gy);
	}
```
and the Kernel Matrix are :

Kernel.IMAGE

the result for BenchMark image :



## CANNY FILTER

this was too Challenging for us but we use the description and helpful DOC of this implementation by tom gibara http://www.tomgibara.com and WIKIPEDIA https://en.wikipedia.org/wiki/Canny_edge_detector

```Java
public CannyFilter(BufferedImage img, float LowThreshold, float HighThreshold) {
		System.out.println("Canny Filter called.");
		this.sourceImage = img;
		if (LowThreshold < 0 || HighThreshold < 0)
			throw new IllegalArgumentException();
		{
			this.lowThreshold = LowThreshold;
			this.highThreshold = HighThreshold;
		}
		lowThreshold = 2.5f;
		highThreshold = 7.5f;
		gaussianKernelRadius = 2f;
		gaussianKernelWidth = 16;
		contrastNormalized = false;
		width = sourceImage.getWidth();
		height = sourceImage.getHeight();
		picsize = width * height;
		initArrays();
		readLuminance();
		if (contrastNormalized)
			normalizeContrast();
		computeGradients(gaussianKernelRadius, gaussianKernelWidth);
		int low = Math.round(lowThreshold * MAGNITUDE_SCALE);
		int high = Math.round(highThreshold * MAGNITUDE_SCALE);
		performHysteresis(low, high);
		thresholdEdges();
		writeEdges(data);
	}

```

the steps are simple as listed in Wikipedia

the result for BenchMark image :


## HOUGH TRANSFORMATION

for hough transformation, we follow the WIKIPEDIA https://en.wikipedia.org/wiki/Hough_transform and http://aishack.in/tutorials/hough-transform-basics/

```Java
public HoughTransform(int[][] inputData, int minContrast) {
		this.minContrast = minContrast;
		HoughTransform.inputMatrix = inputData;
		int width = inputData.length;
		int height = inputData[0].length;
		int maxRadius = (int) Math.ceil(Math.hypot(width, height));
		int halfRAxisSize = inputData.length >>> 1;
		ResultMatrix = new int[inputData[0].length][inputData.length];
		// x output ranges from 0 to pi
		// y output ranges from -maxRadius to maxRadius
		double[] sinTable = new double[inputData[0].length];
		double[] cosTable = new double[inputData[0].length];
		for (int theta = inputData[0].length - 1; theta >= 0; theta--) {
			double thetaRadians = theta * Math.PI / inputData[0].length;
			sinTable[theta] = Math.sin(thetaRadians);
			cosTable[theta] = Math.cos(thetaRadians);
		}
		for (int y = height - 1; y >= 0; y--) {
			for (int x = width - 1; x >= 0; x--) {

				if (contrast(x, y, minContrast)) {
					for (int theta = inputData[0].length - 1; theta >= 0; theta--) {
						double r = cosTable[theta] * x + sinTable[theta] * y;
						int rScaled = (int) Math.round(r * halfRAxisSize / maxRadius) + halfRAxisSize;
						ResultMatrix[theta][rScaled] += 1;
					}
				}

			}
		}
		fixResultMatrix();
		System.out.println("HoughTransform called");
	}

```

the result for BenchMark image :

Contrast 1



Contrast 50



Contrast 100





