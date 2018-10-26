package Filters;

import Basics.OPs;
import Basics.imageIO;

public class SobelFilter {
	
	float[][] kernelMatrix1 = new float[][] { { (float) 1, (float) 0, (float) -1 },
			{ (float) 2, (float) 0, (float) -2 }, { (float) 1, (float) 0, (float) -1 } };
	float[][] kernelMatrix2 = new float[][] { { (float) 1, (float) 2, (float) 1 }, { (float) 0, (float) 0, (float) 0 },
			{ (float) -1, (float) -2, (float) -1 } };
	int imageMatrix[][];
	int kernelMatrixSize;
	private int ResultMatrix[][];
	private int[][] Gx;
	private int[][] Gy;

	public SobelFilter(int imageMatrix[][]) {
		System.out.println("Sobel Filter Called.");
		this.imageMatrix = imageMatrix;
		Gx = OPs.convolution(imageMatrix, kernelMatrix1);
		Gy = OPs.convolution(imageMatrix, kernelMatrix2);
		ResultMatrix=OPs.mergeTwoMatrix(Gx, Gy);
		
	}

	public int[][] getResult() {
		return ResultMatrix;
	}
	public int[][] getGx() {
		return Gx;
	}
	public int[][] getGy() {
		return Gy;
	}
}
