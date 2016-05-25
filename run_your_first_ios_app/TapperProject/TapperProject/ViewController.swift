//
//  ViewController.swift
//  TapperProject
//
//  Copyright © 2016 Holberton School. All rights reserved.
//

import UIKit

class ViewController: UIViewController {
    @IBOutlet weak var image_tapper: UIImageView!
    @IBOutlet weak var button_play: UIButton!
    @IBOutlet weak var textfield_number: UITextField!
    @IBOutlet weak var taps_label: UILabel!
    @IBOutlet weak var button_coin: UIButton!
    var taps_done: Int!
    var taps_requested: Int!
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        taps_done = 0
        taps_requested = 10
        resetGame()
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }
    @IBAction func clickCoinButton(sender: AnyObject) {
        taps_done! += 1
        taps_label.text = String(taps_done) + " taps"
        print("Tap!")
        if taps_done == taps_requested {
            taps_done! = 0
            resetGame()
        }
        
    }


    @IBAction func clickPlayButton(sender: AnyObject) {
        // get number from textfield as string
        let str = textfield_number.text
        // convert to number
        let num = Int(str!)
        // if not number of negative do nothing
        if num < 1 {
            return
        }
        taps_requested = num
        print("let's do " + String(num!) + " taps")
        initGame()
    }
    
    func resetGame() {
        taps_label.hidden = true
        button_coin.hidden = true
        image_tapper.hidden = false
        button_play.hidden = false
        textfield_number.hidden = false
        taps_requested = 0
        taps_done! = 0
    }
    
    func initGame() {
        taps_label.hidden = false
        button_coin.hidden = false
        image_tapper.hidden = true
        button_play.hidden = true
        textfield_number.hidden = true
        taps_label.text = "0 taps"
        taps_done! = 0
    }
}