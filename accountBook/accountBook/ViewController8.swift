//
//  ViewController8.swift
//  accountBook
//
//  Created by 이현수 on 2023/06/30.
//

import UIKit
import Alamofire
class ViewController8: UIViewController {

    @IBOutlet var lbl1: UILabel!
    @IBOutlet var lbl2: UILabel!
    @IBOutlet var lbl3: UILabel!
    override func viewDidLoad() {
        super.viewDidLoad()
        lbl1.text = "사용처"
        lbl2.text = "주소"
        lbl3.text = "총 가격"
        getTest()
        // Do any additional setup after loading the view.
    }
    struct reci: Codable {
                
            var store : String
            var address : String
            var amount: Int
            
        }
    func getTest() {
//         let url = //"http://192.168.10.46:8001/api/recipt"
        let url = "http://192.168.20.147:8000/api/ocr2"
        
         AF.request(url,
                    method: .get,
                    parameters: nil,
                    encoding: URLEncoding.default,
                    headers: ["Content-Type":"application/json", "Accept":"application/json"])
             .validate(statusCode: 200..<300)
             .responseJSON { response in
                 switch response.result {
                 case .success(let value):
                     print(value)
                     
                     
                     
                     
                     do {
                         let data = try JSONSerialization.data(withJSONObject: value, options: .prettyPrinted)
                         let recis = try JSONDecoder().decode(reci.self, from: data)
                         //예){"email" : "hi", "result" : "성공"}
                         self.lbl1.text = "사요엋 : \(recis.store)"
                         self.lbl2.text = "주소 : \(recis.address)"
                         self.lbl3.text = "총 가격 : \(recis.amount)"
                         
                     } catch {
                         
                     }
                     case .failure(let error):
                     break;
                 }
         }
     }

    /*
    // MARK: - Navigation

    // In a storyboard-based application, you will often want to do a little preparation before navigation
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        // Get the new view controller using segue.destination.
        // Pass the selected object to the new view controller.
    }
    */

}
