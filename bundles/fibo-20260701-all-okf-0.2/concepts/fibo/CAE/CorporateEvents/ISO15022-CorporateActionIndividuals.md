---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: This ontology includes the codes for income and corporate action events as specified in ISO 15022, including extensions
      as of 3 September 2020. Scope excludes lower-level notification and meetings related events and message definitions
      associated with ISO 15022 as well as related messages covered by ISO 20022.
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc.\nCopyright (c) 2016-2025 Object Management Group,\
      \ Inc.\n\t\t\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated\
      \ documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the\
      \ rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit\
      \ persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice\
      \ and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE\
      \ IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES\
      \ OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT\
      \ HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,\
      \ ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\n\t\t\
      See https://opensource.org/licenses/MIT."
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: ISO 15022 Corporate Action Individuals Ontology
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2025 Object Management Group, Inc.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - concept: /concepts/fibo/CAE/CorporateEvents/CorporateActions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/CorporateActions/
  - concept: /concepts/fibo/CAE/CorporateEvents/ISO15022-CorporateActionIndividuals.md
    predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/ISO15022-CorporateActionIndividuals/
  - concept: /concepts/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/SecurityRelatedCorporateActions/
  - concept: /concepts/fibo/FBC/DebtAndEquities/CreditEvents.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/CreditEvents/
  - concept: /concepts/fibo/FND/Relations/Relations.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md
    predicate: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/hasMaturityLevel
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Provisional
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Classifiers/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Collections/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/Designators/
resource: https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/ISO15022-CorporateActionIndividuals/
sources:
- id: fibo-source-0762902f25
  resource: references/fibo/CAE/CorporateEvents/ISO15022-CorporateActionIndividuals.rdf
  sha256: 0762902f25fdb491abe0a062189a2924297c4e4fee1441b3df3f3afff5e1fd27
  title: FIBO source CAE/CorporateEvents/ISO15022-CorporateActionIndividuals.rdf
title: ISO 15022 Corporate Action Individuals Ontology
type: Ontology Definition
---

# ISO 15022 Corporate Action Individuals Ontology

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/CAE/CorporateEvents/ISO15022-CorporateActionIndividuals/>

## Relationships

- **Related to**: [CorporateActions](/concepts/fibo/CAE/CorporateEvents/CorporateActions.md)
- **Related to**: [SecurityRelatedCorporateActions](/concepts/fibo/CAE/CorporateEvents/SecurityRelatedCorporateActions.md)
- **Related to**: [CreditEvents](/concepts/fibo/FBC/DebtAndEquities/CreditEvents.md)
- **Related to**: [Relations](/concepts/fibo/FND/Relations/Relations.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [Classifiers](<https://www.omg.org/spec/Commons/Classifiers/>)
- **Related to**: [Collections](<https://www.omg.org/spec/Commons/Collections/>)
- **Related to**: [Designators](<https://www.omg.org/spec/Commons/Designators/>)
- **Related to**: [ISO15022-CorporateActionIndividuals](/concepts/fibo/CAE/CorporateEvents/ISO15022-CorporateActionIndividuals.md)
- **Related to**: [Provisional](/concepts/fibo/FND/Utilities/AnnotationVocabulary/Provisional.md)

## Annotations

- **abstract**: This ontology includes the codes for income and corporate action events as specified in ISO 15022, including extensions as of 3 September 2020. Scope excludes lower-level notification and meetings related events and message definitions associated with ISO 15022 as well as related messages covered by ISO 20022.
- **license**: Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc. Copyright (c) 2016-2025 Object Management Group, Inc. 		 Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 		See https://opensource.org/licenses/MIT.
- **label** (en): ISO 15022 Corporate Action Individuals Ontology
- **copyright**: Copyright (c) 2016-2025 Object Management Group, Inc.
- **copyright**: Copyright (c) 2016-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
