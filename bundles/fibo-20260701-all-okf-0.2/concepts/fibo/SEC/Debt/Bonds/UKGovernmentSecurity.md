---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: U.K. Government security
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: debt instrument issued by HM Treasury and listed on the London Stock Exchange
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: If a private investor wishes to purchase gilts the secondary market can be accessed through a stockbroker, bank
      or the DMO's Purchase and Sale Service.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: 'The term ''gilt'' or ''gilt-edged security'' is a reference to the primary characteristic of gilts as an investment:
      their security. This is a reflection of the fact that the British Government has never failed to make interest or principal
      payments on gilts as they fall due.'
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: gilt
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: gilt-edged security
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.dmo.gov.uk/responsibilities/gilt-market/buying-selling/
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/SovereignDebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignDebtInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/UKGovernmentSecurity
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: U.K. Government security
type: Ontology Class
---

# U.K. Government security

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/UKGovernmentSecurity>

## Definition

debt instrument issued by HM Treasury and listed on the London Stock Exchange

## Relationships

- **See also**: [buying-selling](<https://www.dmo.gov.uk/responsibilities/gilt-market/buying-selling/>)
- **Subclass of**: [SovereignDebtInstrument](/concepts/fibo/SEC/Debt/Bonds/SovereignDebtInstrument.md)

## Annotations

- **label**: U.K. Government security
- **definition**: debt instrument issued by HM Treasury and listed on the London Stock Exchange
- **explanatoryNote**: If a private investor wishes to purchase gilts the secondary market can be accessed through a stockbroker, bank or the DMO's Purchase and Sale Service.
- **explanatoryNote**: The term 'gilt' or 'gilt-edged security' is a reference to the primary characteristic of gilts as an investment: their security. This is a reflection of the fact that the British Government has never failed to make interest or principal payments on gilts as they fall due.
- **synonym**: gilt
- **synonym**: gilt-edged security

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
