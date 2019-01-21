using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace {Example}.ViewModel
{
    public class VmMain : NotificationObject
    {
        public VmMain()
        {
            _text = "Hello Text";
        }

        private string _text;
        public string Text
        {
            set
            {
                _text = value;
                this.RaisePropertyChanged("Text");
            }
            get
            {
                return _text;
            }
        }
    }
}
