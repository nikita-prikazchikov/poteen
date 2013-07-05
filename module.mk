.PHONY: clean
clean:
	rm -rfv $(SOURCE_DIR)/engine/result/data/source/*.json
	rm -rfv $(SOURCE_DIR)/engine/result/data/data.json
	rm -rfv $(SOURCE_DIR)/engine/result/images/*.png
