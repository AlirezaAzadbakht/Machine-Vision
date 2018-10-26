package Basics;

public class OPs {
	public OPs() {

	}

	public static int getMaxElement(int[][] Matrix) {
		int max = Matrix[0][0];
		for (int[] is : Matrix) {
			for (int i : is) {
				if(i>max)
					max=i;
			}
		}
		return max;
	}
	
	public static int[][] mergeTwoMatrix(int[][] imageMatrix1, int[][] imageMatrix2) {
		int[][] ResultMatrix = new int[imageMatrix1.length][imageMatrix1[0].length];
		for (int i = 0; i < imageMatrix1.length; i++) {
			for (int j = 0; j < imageMatrix1[0].length; j++) {
				ResultMatrix[i][j]=(int) Math.sqrt(imageMatrix1[i][j]*imageMatrix1[i][j]+imageMatrix2[i][j]*imageMatrix2[i][j]) ;
			}
		}
		
		return ResultMatrix;
	}
	public static float[][] mirror(int width, int height, float[][] in) {
	    float[][] out = new float[height][width];
	    for (int i = 0; i < height; i++) {
	        for (int j = 0; j < width; j++) {
	            out[i][width - j - 1] = in[i][j];
	        }
	    }
	    return out;
	}

	public static int[][] convolution(int[][] imageMatrix, float[][] kernelMatrix) {
		int kernelMatrixSize = kernelMatrix.length;
		int imageMatrixX = imageMatrix.length;
		int imageMatrixY = imageMatrix[0].length;
		kernelMatrix =mirror(kernelMatrixSize, kernelMatrixSize, kernelMatrix);
		
		int[][] resultMatrix = new int[imageMatrixX][imageMatrixY];
		for (int i = 0; i < imageMatrixX; i++) {
			for (int j = 0; j < imageMatrixY; j++) {
				double temp = 0;
				// in Kernel
				for (int m = 0 ; m < kernelMatrixSize; m++) {
					for (int n = 0; n < kernelMatrixSize; n++) {

						try {
							temp = temp + (kernelMatrix[m][n] * imageMatrix[i-(m-kernelMatrixSize/2)][j+(n-kernelMatrixSize/2)]);
						} catch (Exception e) {
							
						}
						//if(temp>0)
						//System.out.print(kernelMatrix[m][n] +"  "+ imageMatrix[i][j]+" ");

					}
				}
				///////////
				//System.out.println(temp);
				resultMatrix[i][j] = (int) temp;
			}
		}
		System.out.println("Convolution Called.");
		return resultMatrix;

	}
	
	
}
