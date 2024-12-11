git add .
#
echo -n "[+] Enter commit message: " 
read message
if [ -z "$message" ]; then
	message="No commit message"
fi
git commit -m "$message"
git push -u origin main
