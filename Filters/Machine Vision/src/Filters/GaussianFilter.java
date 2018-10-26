package Filters;

public class GaussianFilter {
	int[][] imageMatrix;
	private int[][] ResultMatrix;

	public GaussianFilter(int[][] imageMatrix, int rad, double intens) {

		this.imageMatrix = imageMatrix;
		int height = imageMatrix.length;
		int width = imageMatrix[0].length;
		double norm = 0.;
		
		double invIntensSqrPi = 1 / (Math.sqrt(2 * Math.PI) * intens);
		double[] mask = new double[2 * rad + 1];
		ResultMatrix = new int[height - 2 * rad][width - 2 * rad];

		for (int x = -rad; x < rad + 1; x++) {
			double exp = Math.exp(-((x * x) / 2 * intens * intens));
			mask[x + rad] = invIntensSqrPi * exp;
			norm += mask[x + rad];
		}
		
		for (int r = rad; r < height - rad; r++) {
			for (int c = rad; c < width - rad; c++) {
				double sum = 0.;

				for (int mr = -rad; mr < rad + 1; mr++) {
					sum += (mask[mr + rad] * imageMatrix[r][c + mr]);
				}
				sum /= norm;
				ResultMatrix[r - rad][c - rad] = (int) Math.round(sum);
			}
		}

		for (int r = rad; r < height - rad; r++) {
			for (int c = rad; c < width - rad; c++) {
				double sum = 0.;

				for (int mr = -rad; mr < rad + 1; mr++) {
					sum += (mask[mr + rad] * imageMatrix[r + mr][c]);
				}
				sum /= norm;
				ResultMatrix[r - rad][c - rad] = (int) Math.round(sum);
			}
		}

	}

	public int[][] getResult() {
		return ResultMatrix;
	}

}
