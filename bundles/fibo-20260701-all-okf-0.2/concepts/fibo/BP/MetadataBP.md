---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: "The Business Process (BP) domain includes ontologies that define financial process flows such as securities issuance\
      \ and transaction workflows. In the case of securities issuance process models, these are provided in order to be able\
      \ to represent reference data concepts that are dependent on the process by which a security was issued. Transaction\
      \ process semantics provide the basis for the temporal dimension of securities and derivatives transactions.  These\
      \ are process models represented using basic semantic primitive concepts of events, activities and control flows.\n\t\
      \t\n\t\tNote that the ontologies included in the BP domain are considered provisional and have not undergone serious\
      \ review or integration with other parts of FIBO as of Q1 2026."
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/issued
    value: '2018-08-27T18:00:00'
  - predicate: http://purl.org/dc/terms/license
    value: "Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.\n\nPermission is hereby granted, free of charge,\
      \ to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the\
      \ Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute,\
      \ sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,\
      \ subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in\
      \ all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,\
      \ EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE\
      \ AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\
      \ LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE\
      \ OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\t\t\nSee https://opensource.org/licenses/MIT."
  - datatype: http://www.w3.org/2001/XMLSchema#dateTime
    predicate: http://purl.org/dc/terms/modified
    value: '2026-04-15T18:00:00'
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: Metadata for the FIBO Business Process (BP) Domain
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Ontology
  related_to:
  - predicate: http://www.w3.org/2002/07/owl#versionIRI
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/20260401/MetadataBP/
  - concept: /concepts/fibo/BP/Process/MetadataBPProcess.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/Process/MetadataBPProcess/
  - concept: /concepts/fibo/BP/SecuritiesIssuance/MetadataBPSecuritiesIssuance.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/BP/SecuritiesIssuance/MetadataBPSecuritiesIssuance/
  - concept: /concepts/fibo/FND/Utilities/AnnotationVocabulary.md
    predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/
  - predicate: http://www.w3.org/2002/07/owl#imports
    resource: https://www.omg.org/spec/Commons/AnnotationVocabulary/
resource: https://spec.edmcouncil.org/fibo/ontology/BP/MetadataBP/
sources:
- id: fibo-source-baf045f492
  resource: references/fibo/BP/MetadataBP.rdf
  sha256: baf045f4926f38451d412f3e6fa19bf0cfe399eb712e47c1cb31b6d364c91255
  title: FIBO source BP/MetadataBP.rdf
title: Metadata for the FIBO Business Process (BP) Domain
type: Ontology Definition
---

# Metadata for the FIBO Business Process (BP) Domain

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BP/MetadataBP/>

## Relationships

- **Related to**: [MetadataBPProcess](/concepts/fibo/BP/Process/MetadataBPProcess.md)
- **Related to**: [MetadataBPSecuritiesIssuance](/concepts/fibo/BP/SecuritiesIssuance/MetadataBPSecuritiesIssuance.md)
- **Related to**: [AnnotationVocabulary](/concepts/fibo/FND/Utilities/AnnotationVocabulary.md)
- **Related to**: [AnnotationVocabulary](<https://www.omg.org/spec/Commons/AnnotationVocabulary/>)
- **Related to**: [MetadataBP](<https://spec.edmcouncil.org/fibo/ontology/BP/20260401/MetadataBP/>)

## Annotations

- **abstract**: The Business Process (BP) domain includes ontologies that define financial process flows such as securities issuance and transaction workflows. In the case of securities issuance process models, these are provided in order to be able to represent reference data concepts that are dependent on the process by which a security was issued. Transaction process semantics provide the basis for the temporal dimension of securities and derivatives transactions.  These are process models represented using basic semantic primitive concepts of events, activities and control flows. 		 		Note that the ontologies included in the BP domain are considered provisional and have not undergone serious review or integration with other parts of FIBO as of Q1 2026.
- **issued**: 2018-08-27T18:00:00
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **modified**: 2026-04-15T18:00:00
- **label**: Metadata for the FIBO Business Process (BP) Domain
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
