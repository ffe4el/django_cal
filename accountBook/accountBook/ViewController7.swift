//
//  ViewController7.swift
//  accountBook
//
//  Created by 이현수 on 2023/06/30.
//

import UIKit
import MobileCoreServices
import AVFoundation
import Alamofire
class ViewController7: UIViewController, UINavigationControllerDelegate, UIImagePickerControllerDelegate {
    
    
    

    
    @IBOutlet var btnCamera: UIButton!
    let imagePicker : UIImagePickerController! = UIImagePickerController()
    var captureImage : UIImage!
    var flagImageSave = false
    override func viewDidLoad() {
        super.viewDidLoad()
        postTest()
    }
    
   
    @IBAction func btnCamera1(_ sender: UIButton) {
        if(UIImagePickerController.isSourceTypeAvailable(. camera)){
            flagImageSave = true
            imagePicker.delegate = self
            imagePicker.sourceType = .camera
            imagePicker.mediaTypes = ["public.image"]
            imagePicker.allowsEditing = false
            
            present(imagePicker, animated: true, completion: nil)
            
        }
        
    }
    
    @IBAction func btnAA(_ sender: UIButton) {
    }
    
    
    
    
    
//    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
//        let mediaType = info[UIImagePickerController.InfoKey.mediaType]
//        as! NSString
//
//        if mediaType.isEqual(to: "public.image" as String){
//            captureImage = info[UIImagePickerController.InfoKey.originalImage]
//            as? UIImage
//
//            if flagImageSave {
//                UIImageWriteToSavedPhotosAlbum(captureImage, self, nil, nil)
//            }
//        }
//    }
    func checkCameraPermission(){
        AVCaptureDevice.requestAccess(for: .video, completionHandler: { (granted: Bool) in
            if granted {
                print("Camera: 권한 허용")
            } else {
                print("Camera: 권한 거부")
            }
        })}
    
        
    }

func postTest() {
    let image = UIImage(named: "영수증20.jpg")
    guard let imageData = image?.jpegData(compressionQuality: 0.2) else {
        print("Failed to get image data.")
        return
    }
    let parameters = ["name": "rname"] // Optional for extra parameter
    
    AF.upload(
        multipartFormData: { multipartFormData in
            multipartFormData.append(imageData, withName: "fileupload", fileName: "file.jpg", mimeType: "image/jpeg")
            for (key, value) in parameters {
                multipartFormData.append(value.data(using: .utf8)!, withName: key)
            } // Optional for extra parameters
        },
        to: "http://192.168.20.147:8000/api/upload"
    )
    .uploadProgress { progress in
        print("Upload Progress: \(progress.fractionCompleted)")
    }
    .responseJSON { response in
        switch response.result {
        case .success(let value):
            print(value)
        case .failure(let error):
            print(error)
        }
    }
}
