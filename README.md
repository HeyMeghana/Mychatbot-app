echo "Retrying deployment $(date)" >> README.md
git add README.md
git commit -m "Retrying deployment"
git push origin main
