package Test;

import Basics.OPs;
import Basics.imageIO;

public class conTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		float[][] kernelMatrix = new float[][] { { (float) 0, (float) 0, (float) 0 },
				{ (float) 0, (float) 0, (float) 1 }, { (float) 0, (float) 0, (float) 0 } };
		int[][] k = new int[][] { { 1, 2, 1 }, { 1, 1, 3 }, { 2, 2, 2 } };

		imageIO i = new imageIO();
		int [][] data =OPs.convolution(k, kernelMatrix);
		for (int[] js : data) {
			for (int j : js) {
				System.out.print(j+" ");
			}
			System.out.println();
		}
	}

}
