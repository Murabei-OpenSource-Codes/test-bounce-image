source version
git add --all
git commit -m "Building a new version for Bounce Request Test Image ${VERSION}"
git tag -a ${VERSION} -m "Building a new version for Bounce Request Test Image ${VERSION}"
git push
git push origin ${VERSION}

docker push andrebaceti/bounce-request-test-image:${VERSION}
