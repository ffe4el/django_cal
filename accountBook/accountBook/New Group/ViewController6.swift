//
//  ViewController6.swift
//  accountBook
//
//  Created by 이현수 on 2023/06/29.
//

import UIKit

class ViewController6: UIViewController {

    @IBOutlet var lblbudget: UILabel!
    @IBOutlet var lbl1: UILabel!
    @IBOutlet var lbl2: UILabel!
    @IBOutlet var lbl3: UILabel!
    @IBOutlet var lbl4: UILabel!
    @IBOutlet var lbl5: UILabel!
    @IBOutlet var lbl6: UILabel!
    @IBOutlet var lbl7: UILabel!
    
    @IBOutlet var v8: UIView!
    @IBOutlet var v1: UIView!
    
    @IBOutlet var v9: UIView!

    @IBOutlet var v10: UIView!
    @IBOutlet var v3: UIView!
    @IBOutlet var v4: UIView!
    @IBOutlet var v5: UILabel!
    @IBOutlet var v6: UILabel!
    @IBOutlet var v7: UIView!
   
    @IBOutlet var lbl: UILabel!
    @IBOutlet var v17: UIView!
    @IBOutlet var v16: UIView!
    @IBOutlet var v15: UIView!
    @IBOutlet var v14: UIView!
    @IBOutlet var v13: UIView!
    @IBOutlet var v12: UIView!
    @IBOutlet var v11: UIView!
    @IBOutlet var pg1: UIProgressView!
    override func viewDidLoad() {
        super.viewDidLoad()
        self.lblbudget.text = "2000000"
        // Do any additional setup after loading the view.
        v1.layer.cornerRadius = 20
        v3.layer.cornerRadius = 10
        v4.layer.cornerRadius = 10
        v5.layer.cornerRadius = 10
        v6.layer.cornerRadius = 10
        v7.layer.cornerRadius = 20
        v8.layer.cornerRadius = 20
        v9.layer.cornerRadius = 20
        v10.layer.cornerRadius = 20
        v11.layer.cornerRadius = 20
        v12.layer.cornerRadius = 20
        v13.layer.cornerRadius = 10
        v14.layer.cornerRadius = 10
        v15.layer.cornerRadius = 10
        v16.layer.cornerRadius = 10
        v17.layer.cornerRadius = 10
        pg1.progressViewStyle = .default
        pg1.progressTintColor = .red
        pg1.trackTintColor = .white
        pg1.transform = pg1.transform.scaledBy(x: 1, y: 3)
        lbl1.font = UIFont.boldSystemFont(ofSize: 26)
        lbl2.font = UIFont.boldSystemFont(ofSize: 26)
        lbl3.font = UIFont.boldSystemFont(ofSize: 16)
        lbl4.font = UIFont.boldSystemFont(ofSize: 26)
        lbl5.font = UIFont.boldSystemFont(ofSize: 16)
        lbl6.font = UIFont.boldSystemFont(ofSize: 16)
        lbl7.font = UIFont.boldSystemFont(ofSize: 26)
        
        
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
