//
//  ViewController.swift
//  Django Response Test With Alamofire
//
//  Created by JOHN KENNY on 24/12/2017.
//  Copyright © 2017 JOHN KENNY. All rights reserved.
//

import UIKit
import Alamofire

class ViewController: UIViewController {
    
    

    override func viewDidLoad() {
        super.viewDidLoad()
        
        let urlString = "http://127.0.0.1:8000/requets/"
        
        //request to Django server ---  NB *******Django server Must Be started***********
        Alamofire.request(urlString).response { response in
            // full http response including error codes
            debugPrint(response)
            print("This number should match the nummber in the django terminal \(response.data!)")
            //gets the json array only
        }.responseJSON { response in
                print("This is the json data the server sent")
                print(response)
        }
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }


}

