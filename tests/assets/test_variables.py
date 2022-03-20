from results.nist import NistResult

# take a look at tests/assets/test_results/nist_finalAnalysisReport.txt
# this array contains expected parsed result
NIST_FINAL_ANALYSIS_REPORT_PARSED = [
    NistResult("Frequency", 0.227773,   1.0000),
    NistResult("BlockFrequency", 0.811993,   0.9875),
    NistResult("CumulativeSums", 0.105618,   1.0000),
    NistResult("CumulativeSums", 0.663130,   1.0000),
    NistResult("Runs", 0.186566,   1.0000),
    NistResult("LongestRun", 0.534146,   1.0000),
    NistResult("Rank", 0.414525,   0.9750),
    NistResult("FFT", 0.663130,   1.0000),
    NistResult("NonOverlappingTemplate", 0.392456,   1.0000),
    NistResult("NonOverlappingTemplate", 0.689019,   0.9875),
    NistResult("NonOverlappingTemplate", 0.057146,   1.0000),
    NistResult("NonOverlappingTemplate", 0.484646,   0.9750),
    NistResult("NonOverlappingTemplate", 0.585209,   1.0000),
    NistResult("NonOverlappingTemplate", 0.559523,   0.9875),
    NistResult("NonOverlappingTemplate", 0.258961,   1.0000),
    NistResult("NonOverlappingTemplate", 0.834308,   1.0000),
    NistResult("NonOverlappingTemplate", 0.714660,   1.0000),
    NistResult("NonOverlappingTemplate", 0.437274,   1.0000),
    NistResult("NonOverlappingTemplate", 0.199580,   1.0000),
    NistResult("NonOverlappingTemplate", 0.008120,   1.0000),
    NistResult("NonOverlappingTemplate", 0.311542,   0.9875),
    NistResult("NonOverlappingTemplate", 0.559523,   0.9750),
    NistResult("NonOverlappingTemplate", 0.855534,   1.0000),
    NistResult("NonOverlappingTemplate", 0.078086,   0.9750),
    NistResult("NonOverlappingTemplate", 0.199580,   1.0000),
    NistResult("NonOverlappingTemplate", 0.258961,   1.0000),
    NistResult("NonOverlappingTemplate", 0.788728,   0.9750),
    NistResult("NonOverlappingTemplate", 0.585209,   0.9875),
    NistResult("NonOverlappingTemplate", 0.663130,   0.9875),
    NistResult("NonOverlappingTemplate", 0.611108,   0.9875),
    NistResult("NonOverlappingTemplate", 0.689019,   0.9750),
    NistResult("NonOverlappingTemplate", 0.293235,   0.9750),
    NistResult("NonOverlappingTemplate", 0.509162,   0.9875),
    NistResult("NonOverlappingTemplate", 0.437274,   0.9875),
    NistResult("NonOverlappingTemplate", 0.371101,   1.0000),
    NistResult("NonOverlappingTemplate", 0.559523,   1.0000),
    NistResult("NonOverlappingTemplate", 0.242986,   0.9875),
    NistResult("NonOverlappingTemplate", 0.585209,   1.0000),
    NistResult("NonOverlappingTemplate", 0.834308,   0.9875),
    NistResult("NonOverlappingTemplate", 0.311542,   1.0000),
    NistResult("NonOverlappingTemplate", 0.078086,   1.0000),
    NistResult("NonOverlappingTemplate", 0.811993,   1.0000),
    NistResult("NonOverlappingTemplate", 0.714660,   0.9875),
    NistResult("NonOverlappingTemplate", 0.131500,   1.0000),
    NistResult("NonOverlappingTemplate", 0.788728,   1.0000),
    NistResult("NonOverlappingTemplate", 0.585209,   1.0000),
    NistResult("NonOverlappingTemplate", 0.275709,   1.0000),
    NistResult("NonOverlappingTemplate", 0.213309,   0.9750),
    NistResult("NonOverlappingTemplate", 0.174249,   1.0000),
    NistResult("NonOverlappingTemplate", 0.559523,   0.9875),
    NistResult("NonOverlappingTemplate", 0.258961,   1.0000),
    NistResult("NonOverlappingTemplate", 0.350485,   1.0000),
    NistResult("NonOverlappingTemplate", 0.414525,   1.0000),
    NistResult("NonOverlappingTemplate", 0.105618,   0.9875),
    NistResult("NonOverlappingTemplate", 0.437274,   0.9750),
    NistResult("NonOverlappingTemplate", 0.113706,   0.9875),
    NistResult("NonOverlappingTemplate", 0.460664,   1.0000),
    NistResult("NonOverlappingTemplate", 0.035174,   1.0000),
    NistResult("NonOverlappingTemplate", 0.764655,   0.9875),
    NistResult("NonOverlappingTemplate", 0.585209,   0.9875),
    NistResult("NonOverlappingTemplate", 0.855534,   1.0000),
    NistResult("NonOverlappingTemplate", 0.834308,   1.0000),
    NistResult("NonOverlappingTemplate", 0.611108,   1.0000),
    NistResult("NonOverlappingTemplate", 0.927083,   0.9875),
    NistResult("NonOverlappingTemplate", 0.689019,   0.9750),
    NistResult("NonOverlappingTemplate", 0.484646,   0.9750),
    NistResult("NonOverlappingTemplate", 0.371101,   1.0000),
    NistResult("NonOverlappingTemplate", 0.689019,   1.0000),
    NistResult("NonOverlappingTemplate", 0.764655,   1.0000),
    NistResult("NonOverlappingTemplate", 0.875539,   0.9875),
    NistResult("NonOverlappingTemplate", 0.509162,   1.0000),
    NistResult("NonOverlappingTemplate", 0.811993,   0.9875),
    NistResult("NonOverlappingTemplate", 0.008879,   1.0000),
    NistResult("NonOverlappingTemplate", 0.044942,   0.9750),
    NistResult("NonOverlappingTemplate", 0.986869,   1.0000),
    NistResult("NonOverlappingTemplate", 0.927083,   0.9875),
    NistResult("NonOverlappingTemplate", 0.258961,   0.9750),
    NistResult("NonOverlappingTemplate", 0.559523,   0.9875),
    NistResult("NonOverlappingTemplate", 0.131500,   1.0000),
    NistResult("NonOverlappingTemplate", 0.258961,   1.0000),
    NistResult("NonOverlappingTemplate", 0.460664,   1.0000),
    NistResult("NonOverlappingTemplate", 0.875539,   0.9875),
    NistResult("NonOverlappingTemplate", 0.392456,   1.0000),
    NistResult("NonOverlappingTemplate", 0.875539,   1.0000),
    NistResult("NonOverlappingTemplate", 0.350485,   0.9750),
    NistResult("NonOverlappingTemplate", 0.371101,   0.9875),
    NistResult("NonOverlappingTemplate", 0.953553,   1.0000),
    NistResult("NonOverlappingTemplate", 0.437274,   1.0000),
    NistResult("NonOverlappingTemplate", 0.048716,   0.9875),
    NistResult("NonOverlappingTemplate", 0.875539,   1.0000),
    NistResult("NonOverlappingTemplate", 0.941144,   0.9875),
    NistResult("NonOverlappingTemplate", 0.739918,   0.9750),
    NistResult("NonOverlappingTemplate", 0.330628,   1.0000),
    NistResult("NonOverlappingTemplate", 0.098036,   0.9750),
    NistResult("NonOverlappingTemplate", 0.141256,   1.0000),
    NistResult("NonOverlappingTemplate", 0.894201,   0.9875),
    NistResult("NonOverlappingTemplate", 0.611108,   1.0000),
    NistResult("NonOverlappingTemplate", 0.714660,   0.9875),
    NistResult("NonOverlappingTemplate", 0.788728,   0.9875),
    NistResult("NonOverlappingTemplate", 0.186566,   0.9875),
    NistResult("NonOverlappingTemplate", 0.035174,   1.0000),
    NistResult("NonOverlappingTemplate", 0.611108,   1.0000),
    NistResult("NonOverlappingTemplate", 0.953553,   0.9750),
    NistResult("NonOverlappingTemplate", 0.090936,   1.0000),
    NistResult("NonOverlappingTemplate", 0.559523,   1.0000),
    NistResult("NonOverlappingTemplate", 0.811993,   0.9875),
    NistResult("NonOverlappingTemplate", 0.084294,   1.0000),
    NistResult("NonOverlappingTemplate", 0.788728,   0.9875),
    NistResult("NonOverlappingTemplate", 0.275709,   1.0000),
    NistResult("NonOverlappingTemplate", 0.293235,   1.0000),
    NistResult("NonOverlappingTemplate", 0.098036,   1.0000),
    NistResult("NonOverlappingTemplate", 0.663130,   0.9875),
    NistResult("NonOverlappingTemplate", 0.534146,   0.9875),
    NistResult("NonOverlappingTemplate", 0.991468,   1.0000),
    NistResult("NonOverlappingTemplate", 0.811993,   1.0000),
    NistResult("NonOverlappingTemplate", 0.186566,   0.9625),
    NistResult("NonOverlappingTemplate", 0.293235,   1.0000),
    NistResult("NonOverlappingTemplate", 0.637119,   0.9875),
    NistResult("NonOverlappingTemplate", 0.242986,   0.9750),
    NistResult("NonOverlappingTemplate", 0.637119,   1.0000),
    NistResult("NonOverlappingTemplate", 0.038187,   0.9750),
    NistResult("NonOverlappingTemplate", 0.559523,   0.9875),
    NistResult("NonOverlappingTemplate", 0.258961,   0.9750),
    NistResult("NonOverlappingTemplate", 0.739918,   1.0000),
    NistResult("NonOverlappingTemplate", 0.437274,   0.9875),
    NistResult("NonOverlappingTemplate", 0.174249,   1.0000),
    NistResult("NonOverlappingTemplate", 0.611108,   1.0000),
    NistResult("NonOverlappingTemplate", 0.714660,   1.0000),
    NistResult("NonOverlappingTemplate", 0.392456,   0.9875),
    NistResult("NonOverlappingTemplate", 0.611108,   1.0000),
    NistResult("NonOverlappingTemplate", 0.392456,   1.0000),
    NistResult("NonOverlappingTemplate", 0.113706,   0.9750),
    NistResult("NonOverlappingTemplate", 0.213309,   0.9875),
    NistResult("NonOverlappingTemplate", 0.003261,   1.0000),
    NistResult("NonOverlappingTemplate", 0.788728,   1.0000),
    NistResult("NonOverlappingTemplate", 0.186566,   0.9750),
    NistResult("NonOverlappingTemplate", 0.151616,   0.9750),
    NistResult("NonOverlappingTemplate", 0.663130,   1.0000),
    NistResult("NonOverlappingTemplate", 0.689019,   0.9875),
    NistResult("NonOverlappingTemplate", 0.875539,   0.9875),
    NistResult("NonOverlappingTemplate", 0.460664,   1.0000),
    NistResult("NonOverlappingTemplate", 0.311542,   1.0000),
    NistResult("NonOverlappingTemplate", 0.637119,   0.9750),
    NistResult("NonOverlappingTemplate", 0.330628,   1.0000),
    NistResult("NonOverlappingTemplate", 0.585209,   1.0000),
    NistResult("NonOverlappingTemplate", 0.980883,   0.9875),
    NistResult("NonOverlappingTemplate", 0.371101,   0.9750),
    NistResult("NonOverlappingTemplate", 0.834308,   0.9625),
    NistResult("NonOverlappingTemplate", 0.509162,   1.0000),
    NistResult("NonOverlappingTemplate", 0.052778,   0.9875),
    NistResult("NonOverlappingTemplate", 0.973388,   0.9875),
    NistResult("NonOverlappingTemplate", 0.689019,   1.0000),
    NistResult("NonOverlappingTemplate", 0.437274,   0.9875),
    NistResult("NonOverlappingTemplate", 0.534146,   1.0000),
    NistResult("NonOverlappingTemplate", 0.764655,   1.0000),
    NistResult("NonOverlappingTemplate", 0.875539,   0.9875),
    NistResult("OverlappingTemplate", 0.534146,   1.0000),
    NistResult("Universal", 0.941144,   0.9750),
    NistResult("ApproximateEntropy", 0.611108,   1.0000),
    NistResult("RandomExcursions", 0.987896,   0.9608),
    NistResult("RandomExcursions", 0.474986,   0.9608),
    NistResult("RandomExcursions", 0.304126,   0.9804),
    NistResult("RandomExcursions", 0.554420,   0.9804),
    NistResult("RandomExcursions", 0.946308,   1.0000),
    NistResult("RandomExcursions", 0.946308,   1.0000),
    NistResult("RandomExcursions", 0.678686,   1.0000),
    NistResult("RandomExcursions", 0.334538,   1.0000),
    NistResult("RandomExcursionsVariant", 0.249284,   1.0000),
    NistResult("RandomExcursionsVariant", 0.202268,   1.0000),
    NistResult("RandomExcursionsVariant", 0.202268,   1.0000),
    NistResult("RandomExcursionsVariant", 0.275709,   0.9804),
    NistResult("RandomExcursionsVariant", 0.401199,   0.9608),
    NistResult("RandomExcursionsVariant", 0.759756,   0.9608),
    NistResult("RandomExcursionsVariant", 0.678686,   0.9608),
    NistResult("RandomExcursionsVariant", 0.637119,   0.9608),
    NistResult("RandomExcursionsVariant", 0.514124,   0.9804),
    NistResult("RandomExcursionsVariant", 0.334538,   0.9804),
    NistResult("RandomExcursionsVariant", 0.595549,   0.9804),
    NistResult("RandomExcursionsVariant", 0.678686,   0.9608),
    NistResult("RandomExcursionsVariant", 0.897763,   0.9804),
    NistResult("RandomExcursionsVariant", 0.946308,   1.0000),
    NistResult("RandomExcursionsVariant", 0.554420,   1.0000),
    NistResult("RandomExcursionsVariant", 0.964295,   1.0000),
    NistResult("RandomExcursionsVariant", 0.514124,   0.9804),
    NistResult("RandomExcursionsVariant", 0.249284,   0.9804),
    NistResult("Serial", 0.227773,   0.9875),
    NistResult("Serial", 0.199580,   0.9875),
    NistResult("LinearComplexity", 0.213309,   0.9875),
]
