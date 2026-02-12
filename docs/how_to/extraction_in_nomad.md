# Running extraction in NOMAD

The NOMAD [Perovskite Solar Cells Database plugin](https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database) allows users to extract solar cell data from scientific publications uploaded to the NOMAD platform. This guide provides step-by-step instructions for running the extraction workflow.

## Requirements

Data extraction can be run in central [NOMAD](https://nomad-lab.eu/prod/v1/gui), [Test Oasis](https://nomad-lab.eu/prod/v1/oasis/gui) or in any NOMAD deployment that:

- has the NOMAD [Perovskite Solar Cells Database plugin](https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database) installed
- supports NOMAD [Actions](https://nomad-lab.eu/prod/v1/docs/howto/plugins/types/actions.html) and has a CPU task queue with corresponding worker(s) running

Publications must be uploaded in PDF format. An API key for one of the supported large language models (LLMs) is also required.

## Running the extraction

Open the central NOMAD:

```
https://nomad-lab.eu/prod/v1/gui
```

Log in, then navigate to `PUBLISH/Uploads`, create a new empty upload, and add the PDF files of the publications to be processed.

After the files have been uploaded, use `CREATE FROM SCHEMA` to add a new entry that will be used to process the PDFs. In the dialog window that appears, give the entry a name and select the built-in schema called `LLM Perovskite Paper Extractor`, then click `CREATE`.

You will be redirected to the `DATA` tab of the newly created entry, where a list of the previously uploaded publications should be visible. Additional files can be added at this stage by clicking the upload symbol on the right-hand side of the `Upload PDF files ...` field.

Next, choose a model from the list of available LLMs and enter the corresponding API key. Finally, click the `RUN LLM EXTRACTION ACTION` button to start the extraction process.

The entry will update to show a new *triggered action* subsection, including the action id and current status. The action typically runs for several minutes, with the duration depending on the number and size of the uploaded PDF files. During execution, the extractor attempts to identify all solar cells described in the publications and creates a new NOMAD entry for each one. After successful processing, the source PDF files are deleted.

<video controls autoplay loop muted playsinline width="100%">
  <source src="../../assets/videos/LLM_Extraction_ELN_start_action.webm" type="video/webm">
  Your browser does not support the video tag.
</video>

You can monitor the status of the action by clicking `GET ACTION STATUS`. Once the status is `COMPLETED`, the list of extracted solar cells will appear under *extracted solar cells* as `LLMExtractedPerovskiteSolarCell` entries. These newly created entries and their normalized form `PerovskiteSolarCell` (compatible with the perovskite database) can also be accessed by returning to the upload overview and selecting them from the list available under `2 Process data`.

<video controls autoplay loop muted playsinline width="100%">
  <source src="../../assets/videos/LLM_Extraction_ELN_results.webm" type="video/webm">
  Your browser does not support the video tag.
</video>

!!! note

    It is also possible to run the NOMAD Action directly without creating an `LLM Perovskite Paper Extractor` entry. This option is available only in the new [NOMAD GUI](https://nomad-lab.eu/prod/v1/gui/v2/) (currently in beta). Create a project, upload the publication files, then click `RUN ACTION`, select `LLMExtractionAction`, and fill in the form that appears. The results of the extraction will be shown directly within the project.