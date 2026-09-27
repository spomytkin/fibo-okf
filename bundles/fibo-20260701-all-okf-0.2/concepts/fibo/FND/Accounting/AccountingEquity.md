---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology defines equity-related concepts for use in defining other FIBO ontology elements. These are based
      on basic accounting principles as they relate to equity, debt, assets and liabilities of a firm. Equity forms the basis
      for ownership of certain forms of corporate body.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2013-2025 Object Management Group,\
      \ Inc.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\t\
      See https://opensource.org/licenses/MIT."
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Accounting Equity Ontology
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: "The http://www.omg.org/spec/FIBO/Foundations/20130601/Accounting/AccountingEquity.owl version of the ontology\
      \ was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:\n   (1) to use slash style URI/IRIss\
      \ (also called 303 URIs, vs. hash style) as required to support server side processing \n   (2) to use version-independent\
      \ IRIs for all definitions internally as opposed to version-specific IRIs\n   (3) to change the file suffix from .owl\
      \ to .rdf to increase usability in RDF tools\n   (4) to use 4-level abbreviations and corresponding namespace prefixes\
      \ for all FIBO ontologies, reflecting a family/specification/module/ontology structure\n   (5) to incorporate changes\
      \ to the specification metadata to support documentation at the family, specification, module, and ontology level, similar\
      \ to the abbreviations."
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/Accounting/AccountingEquity.rdf version of this ontology
      was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Accounting/AccountingEquity.rdf version of this ontology
      was modified per the issue resolutions identified in the FIBO FND 1.1 RTF report, namely, to rename MoneyAmount to AmountOfMoney
      and replace it herein with MonetaryAmount, as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Accounting/AccountingEquity.rdf version of this ontology
      was modified per the FIBO 2.0 RFC to rework definitions in support of revised Business Entities, Equities and related
      ontologies.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Accounting/AccountingEquity.rdf version of this ontology
      was modified to eliminate deprecated elements.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Accounting/AccountingEquity.rdf version of this ontology
      was modified to augment the definition of asset, and add income.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20200101/Accounting/AccountingEquity.rdf version of this ontology
      was modified to add physical asset and eliminate ambiguity in some definitions.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20201001/Accounting/AccountingEquity.rdf version of this ontology
      was modified to fix spelling errors and deprecate the property represents an interest in, which is not used elsewhere
      and is confusing.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/Accounting/AccountingEquity.rdf version of this ontology
      was modified to make income a subclass of monetary amount and eliminate the oblique restriction on monetary amount to
      simplify its representation.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220301/Accounting/AccountingEquity.rdf version of this ontology
      was modified to eliminate the deprecated 'represents an interest in' property.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20220401/Accounting/AccountingEquity.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification
      Metadata vocabulary.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Accounting/AccountingEquity.rdf version of this ontology
      was modified to add a definition for EBITDA.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Accounting/AccountingEquity.rdf version of this ontology
      was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC),
      eliminating redundancies in FIBO as appropriate.
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20230601/Accounting/AccountingEquity.rdf version of this ontology
      was modified to correct the definition of EBITDA and to replace content that is now available in the OMG Commons Ontology
      Library (Commons) v1.1 (FND-380).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Accounting/AccountingEquity.rdf version of the ontology
      was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2
      (FND-389).
  - predicate: http://www.w3.org/2004/02/skos/core#changeNote
    value: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Accounting/AccountingEquity.rdf version of the ontology
      was modified to move the concepts that were originally defined herein to the ownership ontology to improve usability
      (FND-409). Note that this ontology and all of its deprecated concepts will be eliminated in the Q2 2027 release.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Accounting/AccountingEquity/
  - concept: /concepts/fibo/FND/OwnershipAndControl/Ownership.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/OwnershipAndControl/Ownership/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Release
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
resource: https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/AccountingEquity/
sources:
- id: fibo-source-7cd2615fdd
  resource: references/fibo/FND/Accounting/AccountingEquity.rdf
  sha256: 7cd2615fdde64d9064cd66e02f88718bb214bdc1cf57acc98f85a6355d01fdb8
  title: FIBO source FND/Accounting/AccountingEquity.rdf
title: Accounting Equity Ontology
type: Ontology Definition
---

# Accounting Equity Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FND/Accounting/AccountingEquity/>

## Relationships

- **Related to**: [Ownership](/concepts/fibo/FND/OwnershipAndControl/Ownership.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [AccountingEquity](<https://spec.edmcouncil.org/fibo/ontology/FND/20260701/Accounting/AccountingEquity/>)
- **Related to**: [Release](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Release.md)

## Annotations

- **abstract**: This ontology defines equity-related concepts for use in defining other FIBO ontology elements. These are based on basic accounting principles as they relate to equity, debt, assets and liabilities of a firm. Equity forms the basis for ownership of certain forms of corporate body.
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2013-2025 Object Management Group, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label**: Accounting Equity Ontology
- **changeNote**: The http://www.omg.org/spec/FIBO/Foundations/20130601/Accounting/AccountingEquity.owl version of the ontology was revised in advance of the September 2013 New Brunswick, NJ meeting, as follows:    (1) to use slash style URI/IRIss (also called 303 URIs, vs. hash style) as required to support server side processing     (2) to use version-independent IRIs for all definitions internally as opposed to version-specific IRIs    (3) to change the file suffix from .owl to .rdf to increase usability in RDF tools    (4) to use 4-level abbreviations and corresponding namespace prefixes for all FIBO ontologies, reflecting a family/specification/module/ontology structure    (5) to incorporate changes to the specification metadata to support documentation at the family, specification, module, and ontology level, similar to the abbreviations.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20130801/Accounting/AccountingEquity.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FND 1.0 FTF report and in https://spec.edmcouncil.org/fibo/ontology/FND/1.0/AboutFND-1.0/.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20141101/Accounting/AccountingEquity.rdf version of this ontology was modified per the issue resolutions identified in the FIBO FND 1.1 RTF report, namely, to rename MoneyAmount to AmountOfMoney and replace it herein with MonetaryAmount, as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20160201/Accounting/AccountingEquity.rdf version of this ontology was modified per the FIBO 2.0 RFC to rework definitions in support of revised Business Entities, Equities and related ontologies.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20180801/Accounting/AccountingEquity.rdf version of this ontology was modified to eliminate deprecated elements.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20190901/Accounting/AccountingEquity.rdf version of this ontology was modified to augment the definition of asset, and add income.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20200101/Accounting/AccountingEquity.rdf version of this ontology was modified to add physical asset and eliminate ambiguity in some definitions.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20201001/Accounting/AccountingEquity.rdf version of this ontology was modified to fix spelling errors and deprecate the property represents an interest in, which is not used elsewhere and is confusing.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20211201/Accounting/AccountingEquity.rdf version of this ontology was modified to make income a subclass of monetary amount and eliminate the oblique restriction on monetary amount to simplify its representation.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220301/Accounting/AccountingEquity.rdf version of this ontology was modified to eliminate the deprecated 'represents an interest in' property.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20220401/Accounting/AccountingEquity.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) Annotation Vocabulary rather than the OMG's Specification Metadata vocabulary.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Accounting/AccountingEquity.rdf version of this ontology was modified to add a definition for EBITDA.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230101/Accounting/AccountingEquity.rdf version of this ontology was modified to use the Commons Ontology Library (Commons) rather than the OMG's Languages, Countries and Codes (LCC), eliminating redundancies in FIBO as appropriate.
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20230601/Accounting/AccountingEquity.rdf version of this ontology was modified to correct the definition of EBITDA and to replace content that is now available in the OMG Commons Ontology Library (Commons) v1.1 (FND-380).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20231201/Accounting/AccountingEquity.rdf version of the ontology was modified to replace additional content that is now available in the OMG Commons Ontology Library (Commons) v1.2 (FND-389).
- **changeNote**: The https://spec.edmcouncil.org/fibo/ontology/FND/20250301/Accounting/AccountingEquity.rdf version of the ontology was modified to move the concepts that were originally defined herein to the ownership ontology to improve usability (FND-409). Note that this ontology and all of its deprecated concepts will be eliminated in the Q2 2027 release.
- **copyright**: Copyright (c) 2013-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
