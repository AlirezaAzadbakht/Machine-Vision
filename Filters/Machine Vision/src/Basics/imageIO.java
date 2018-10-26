package Basics;

import java.io.*;
import java.awt.*;
import java.awt.image.*;

import javax.imageio.ImageIO;
import javax.swing.*;

public class imageIO {

	public imageIO() {
	}

	public BufferedImage MatrixtoImage(int[][] imageMatrix , double scale) {
		BufferedImage image = new BufferedImage(imageMatrix.length, imageMatrix[0].length, BufferedImage.TYPE_INT_RGB);
		// try {
		// for (int i = 0; i < imageMatrix.length; i++) {
		// for (int j = 0; j < imageMatrix[0].length; j++) {
		// image.setRGB(i, j, new Color(imageMatrix[i][j], imageMatrix[i][j],
		// imageMatrix[i][j]).getRGB());
		// }
		// }
		// System.out.println("Converting Matrix to image.");
		// } catch (Exception e) {
		// // TODO: handle exception
		// System.out.println("Error: Matrix to image" + e);
		// }
		for (int i = 1; i < imageMatrix.length; i++) {
			for (int j = 1; j < imageMatrix[0].length; j++) {
				int edgeColor = imageMatrix[i][j];
				edgeColor = (int) (edgeColor * scale);
				edgeColor = 0xff000000 | (edgeColor << 16) | (edgeColor << 8) | edgeColor;

				image.setRGB(i, j, edgeColor);
			}
		}

		return image;

	}

	public int[][] GetImageMatrix(BufferedImage image) {
		int imagematrix[][] = new int[image.getWidth()][image.getHeight()];
		try {

			for (int i = 0; i < image.getWidth(); i++) {

				for (int j = 0; j < image.getHeight(); j++) {
					int rgb = image.getRGB(i , j);
					int r = (rgb >> 16) & 0xff;
			        int g = (rgb >> 8) & 0xff;
			        int b = (rgb) & 0xff;
			        int gray = (int)(0.2126 * r + 0.7152 * g + 0.0722 * b);
			        
					imagematrix[i][j] = gray;
				}
			}
			System.out.println("Converting image to Matrix.");

		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("Error: 22 " + e);
		}

		return imagematrix;

	}

	public BufferedImage LoadImage(File file) {
		BufferedImage image = null;
		try {
			image = ImageIO.read(file);
			System.out.println("Loading complete.");
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("Error: " + e);
		}
		return image;
	}

	public void SaveImage(BufferedImage image, File file) {
		try {
			ImageIO.write(image, "png", file);
			System.out.println("Saving complete.");
		} catch (IOException e) {
			// TODO: handle exception
			System.out.println("Error: " + e);
		}
	}

	public void ShowImage(BufferedImage image) {
		try {
			JLabel picLabel = new JLabel(new ImageIcon(image));
			JPanel jpanel = new JPanel();
			jpanel.add(picLabel);
			JFrame frame = new JFrame();
			// frame.setSize(new Dimension(image.getWidth(),
			// image.getHeight()));
			frame.setSize(new Dimension(500, 500));
			frame.add(jpanel);
			frame.setVisible(true);
			System.out.println("Showing Image.");
		} catch (Exception e) {
			// TODO: handle exception
			System.out.println("Error: 1" + e);
		}
	}
}
