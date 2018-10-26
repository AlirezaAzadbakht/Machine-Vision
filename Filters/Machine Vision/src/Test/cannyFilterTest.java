package Test;

import java.awt.image.BufferedImage;
import java.io.File;

import Basics.imageIO;
import Filters.CannyFilter;
import Filters.SobelFilter;

public class cannyFilterTest {

	public static void main(String[] args) {
		File file = new File("C:\\Users\\Alireza\\Pictures\\profile pics\\1o2.jpg");
		imageIO i = new imageIO();
		BufferedImage img = i.LoadImage(file);
		i.ShowImage(img);

		BufferedImage Result = new CannyFilter(img, 0.5f, 1f).getResult();
		i.ShowImage(Result);
		//i.SaveImage(Result, new File("C:\\Users\\Alireza\\Pictures\\profile pics\\CannyResult.jpg"));
	}

}
