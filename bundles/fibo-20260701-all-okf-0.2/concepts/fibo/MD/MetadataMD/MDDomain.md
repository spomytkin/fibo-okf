---
owl:
  annotations:
  - predicate: http://purl.org/dc/terms/abstract
    value: "The Market Data (MD) domain contains ontologies that represent temporally variant concepts for financial instruments,\
      \ loans and funds. As such this domain covers the concepts represented in market data, such as prices, yields and analytics\
      \ for debt and for pools of assets.\n\t\t\n\t\tNote that the ontologies included in the MD domain are considered provisional\
      \ and have not undergone serious review or integration with other parts of FIBO as of Q1 2026."
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
  - predicate: http://purl.org/dc/terms/title
    value: Financial Industry Business Ontology (FIBO) Market Data (MD) Domain
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: market data domain
  - datatype: http://www.w3.org/2001/XMLSchema#anyURI
    predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    value: https://spec.edmcouncil.org/fibo/
  - predicate: http://www.w3.org/2004/02/skos/core#altLabel
    value: Market Data (MD)
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/copyright
    value: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.
  rdf_types:
  - http://www.w3.org/2002/07/owl#NamedIndividual
  - https://spec.edmcouncil.org/fibo/ontology/FND/Utilities/AnnotationVocabulary/Module
  related_to:
  - concept: /concepts/fibo/MD/CIVTemporal/MetadataMDCIVTemporal/CIVTemporalModule.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/CIVTemporal/MetadataMDCIVTemporal/CIVTemporalModule
  - concept: /concepts/fibo/MD/DebtTemporal/MetadataMDDebtTemporal/DebtTemporalModule.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DebtTemporal/MetadataMDDebtTemporal/DebtTemporalModule
  - concept: /concepts/fibo/MD/DerivativesTemporal/MetadataMDDerivativesTemporal/DerivativesTemporalModule.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/DerivativesTemporal/MetadataMDDerivativesTemporal/DerivativesTemporalModule
  - concept: /concepts/fibo/MD/TemporalCore/MetadataMDTemporalCore/TemporalCoreModule.md
    predicate: http://purl.org/dc/terms/hasPart
    resource: https://spec.edmcouncil.org/fibo/ontology/MD/TemporalCore/MetadataMDTemporalCore/TemporalCoreModule
resource: https://spec.edmcouncil.org/fibo/ontology/MD/MetadataMD/MDDomain
sources:
- id: fibo-source-b115b15c4e
  resource: references/fibo/MD/MetadataMD.rdf
  sha256: b115b15c4e5309ec4e4e03f58c500a747f103c4df964cbec40a63ecb0d621ff0
  title: FIBO source MD/MetadataMD.rdf
title: market data domain
type: Ontology Individual
---

# market data domain

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/MD/MetadataMD/MDDomain>

## Synonyms

- Market Data (MD)

## Relationships

- **Related to**: [CIVTemporalModule](/concepts/fibo/MD/CIVTemporal/MetadataMDCIVTemporal/CIVTemporalModule.md)
- **Related to**: [DebtTemporalModule](/concepts/fibo/MD/DebtTemporal/MetadataMDDebtTemporal/DebtTemporalModule.md)
- **Related to**: [DerivativesTemporalModule](/concepts/fibo/MD/DerivativesTemporal/MetadataMDDerivativesTemporal/DerivativesTemporalModule.md)
- **Related to**: [TemporalCoreModule](/concepts/fibo/MD/TemporalCore/MetadataMDTemporalCore/TemporalCoreModule.md)

## Annotations

- **abstract**: The Market Data (MD) domain contains ontologies that represent temporally variant concepts for financial instruments, loans and funds. As such this domain covers the concepts represented in market data, such as prices, yields and analytics for debt and for pools of assets. 		 		Note that the ontologies included in the MD domain are considered provisional and have not undergone serious review or integration with other parts of FIBO as of Q1 2026.
- **issued**: 2018-08-27T18:00:00
- **license**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.  Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:  The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.  THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 		 See https://opensource.org/licenses/MIT.
- **modified**: 2026-04-15T18:00:00
- **title**: Financial Industry Business Ontology (FIBO) Market Data (MD) Domain
- **label**: market data domain
- **seeAlso**: https://spec.edmcouncil.org/fibo/
- **altLabel**: Market Data (MD)
- **copyright**: Copyright (c) 2013-2026 EDM Association dba EDM Council, Inc.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
