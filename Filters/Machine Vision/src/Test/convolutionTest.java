package Test;

import java.awt.image.BufferedImage;
import java.io.File;

import Basics.*;

public class convolutionTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		
		
		
		imageIO i = new imageIO();

		float[][] kernelMatrix = new float[][] { { (float) 1 / 9, (float) 1 / 9, (float) 1 / 9 },
				{ (float) 1 / 9, (float) 1 / 9, (float) 1 / 9 }, { (float) 1 / 9, (float) 1 / 9, (float) 1 / 9 } };
		
		
		File file = new File("C:\\Users\\Alireza\\Pictures\\profile pics\\1o2.jpg");
		BufferedImage img;
		img = i.LoadImage(file);
		i.ShowImage(img);
		int[][] data = i.GetImageMatrix(img);
		data = OPs.convolution(data, kernelMatrix);
		img = i.MatrixtoImage(data,1);
		i.ShowImage(img);
		//i.SaveImage(img, new File("C:\\Users\\Alireza\\Pictures\\profile pics\\ConvolutionResult.jpg"));
	}

}
