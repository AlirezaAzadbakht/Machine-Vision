package Filters;

import Basics.OPs;

public class HoughTransform {
	int minContrast;
	private static int[][] ResultMatrix;
	private static int[][] inputMatrix;

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

	public int[][] getResult() {
		return ResultMatrix;
	}

	public boolean contrast(int x, int y, int minContrast) {
		int centerValue = inputMatrix[x][y];
		for (int i = 8; i >= 0; i--) {
			if (i == 4)
				continue;
			int newx = x + (i % 3) - 1;
			int newy = y + (i / 3) - 1;
			if ((newx < 0) || (newx >= inputMatrix.length) || (newy < 0) || (newy >= inputMatrix[0].length))
				continue;
			if (Math.abs(inputMatrix[newx][newy] - centerValue) >= minContrast)
				return true;
		}
		return false;
	}

	public static void fixResultMatrix() {
		int max = OPs.getMaxElement(ResultMatrix);
		for (int y = 0; y < ResultMatrix[0].length; y++) {
			for (int x = 0; x < ResultMatrix.length; x++) {
				int n = Math.min((int) Math.round(ResultMatrix[x][y] * 255.0 / max), 255);
				ResultMatrix[x][y] = n;
			}
		}
	}

}
