# Run extraction in NOMAD

NOMAD Perovskite Solar Cells Database plugin allows users to extract solar cells data from scientific publications uploaded to NOMAD. This guide provides step-by-step instructions for running the extraction.

## Requirements

The data extraction can be run in central Test Oasis or any NOMAD deployment that

- has NOMAD Perovskite Solar Cells Database plugin installed
- supports NOMAD Actions and has CPU task queue with corresponding worker(s) running

The publications must be uploaded in pdf format. An API key for one of the supported models is also required.

## Running extraction

Open Test Oasis:

```
https://nomad-lab.eu/prod/v1/oasis/gui
```

and navigate to `PUBLISH/Uploads`. Create a new empty upload, and add the pdf files of the publications for extraction.

After the files has been uploaded, use `CREATE FROM SCHEMA` to add a new entry that will be used to process the pdf files. In the appearing dialog window, give the entry any name and select a built-in schema `LLM Perovskite Paper Extractor`, then click `CREATE`.

You will be brought to the `DATA` tab of the new entry. You should be able to see the list of previously uploaded publications. You can also add more files now by clicking on the upload symbol at the right side of the `Upload PDF files ...` field. After that choose a model from the list of available LLMs for processing, and enter an API key for access to the model. Finally, click `RUN LLM EXTRACTION ACTION` button to start the process.

The entry will update showing a new `triggered action` subsection with action id and status displayed. The action will run for typically several minutes, the time depending on the number and size of pdf files uploaded. It will attempt to extract all solar cells described in the publications and create a new entry for each one, then delete the source pdf files. You can check the status of the action by clicking `GET ACTION STATUS`; once the status is `COMPLETED`, the list of extracted solar cells should appear under `extracted solar cells`. You can also directly access the new entries by going back to the upload overview and selecting from the list available under `2 Process data`.