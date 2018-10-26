package Test;

import java.awt.image.BufferedImage;
import java.io.File;

import Basics.imageIO;
import Filters.HoughTransform;
import Filters.SobelFilter;

public class houghTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		imageIO i = new imageIO();		
		File file = new File("C:\\Users\\Alireza\\Pictures\\profile pics\\1o2.jpg");
		BufferedImage img;
		img = i.LoadImage(file);
		i.ShowImage(img);
		int[][] data = i.GetImageMatrix(img);
	
		data =  new HoughTransform(data,100).getResult();
		img = i.MatrixtoImage(data,1);
		i.ShowImage(img);
		//i.SaveImage(img, new File("C:\\Users\\Alireza\\Pictures\\profile pics\\HoughResultC100.jpg"));

	}

}
