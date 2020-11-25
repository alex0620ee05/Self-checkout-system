#include <glog/logging.h>
#include <iostream>
#include <memory>
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <vitis/ai/nnpp/ssd.hpp>
#include <vitis/ai/demo.hpp>
#include "./process_result.hpp"
#include <vector>
#include <cstring>
#include <vitis/ai/tfssd.hpp>
#include <ctime>
#include <typeinfo>
extern "C"
{
    auto ssd = vitis::ai::TFSSD::create("ssd_mobilenet_v2_coco_tf", true); 
    int process(int height, int width, uchar* frame_data,float *a_pt)
    {
	clock_t start;
	//start = clock();
        int count = 0;
        std::vector<float> detection_list;
        cv::Mat image(height, width, CV_8UC3);
        uchar* pxvec =image.ptr<uchar>(0);
        
        for(int row = 0; row < height; row++)
        {
            pxvec = image.ptr<uchar>(row);
            for(int col = 0; col < width; col++)
            {
                for(int c = 0; c < 3; c++)
                {
                    pxvec[col*3+c] = frame_data[count];  
                    count++  ;                
                }
            }
        }
        count =0;
	//std::cout<<clock()<<std::endl;
	//std::cout<<"preprocess time:"<<clock()-start<<std::endl;
	//start = clock(); 
	//std::cout<<clock()<<std::endl;
         //auto ssd = vitis::ai::TFSSD::create("ssd_mobilenet_v1_coco_tf", true);          
         auto results = ssd->run(image);
	//std::cout<<"DPU time:"<<clock()-start<<std::endl;
        //start = clock(); 
	for(const auto &r : results.bboxes){
           auto label = r.label;
           auto x = r.x * width;//image.cols;
           auto y = r.y * height;//image.rows;
           auto width_ = x+r.width * width;//image.cols;
           auto heigth_ = y+r.height * height;//image.rows;
           auto score = r.score;
           if (count >= 120)break;
	   if (label == 44 || label == 47 || label == 48 || label == 50 ||label == 51 || label ==52 || label == 53 || label == 55 || label == 58 || label == 60 || label == 87){ 
	   //bottle , cup ,fork , spoon , bowl , banana , apple ,orange ,hotdog , donut , scissors;
           count+=6;
           //std::cout << "RESULT: " << label << "\t" << x << "\t" << y << "\t" <<width_ << "\t" << heigth_ << "\t" << score << std::endl;
           detection_list.push_back(label);
           detection_list.push_back(x);
           detection_list.push_back(y);
           detection_list.push_back(width_);
           detection_list.push_back(heigth_);
           detection_list.push_back(score);
	   }
        } 
        std::memcpy(a_pt,detection_list.data(),detection_list.size()*sizeof detection_list[0]); 
        //imshow("result", image);
        //waitKey(0);
        //std::cout<<"postprocess time:"<<clock()-start<<std::endl;
        return count;
    }
}
