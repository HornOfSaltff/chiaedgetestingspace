hash=$(git rev-parse --short HEAD)
docker build --platform linux/arm64 -t ecy14mhfh/pihattest:$hash -f Dockerfile .
docker push ecy14mhfh/pihattest:$hash
echo $hash