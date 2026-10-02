---
owl:
  annotations:
  - language: en
    predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: participation instrument
  - language: en
    predicate: http://www.w3.org/2004/02/skos/core#definition
    value: structured product that provides the possibility to participate in the performance of an asset or basket of assets
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/adaptedFrom
    value: ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth
      edition, 2021-06-15
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: The construction is generally based on a low exercise price option (LEPO) (base value less discounted future dividends)
      which in some cases might be comparable to a direct investment in the underlying asset(s) or a LEPO combined with other
      options, which together provide the desired disbursement profile.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: These assets could be anything, from equities, funds, bonds, ETFs indices to a mix of those. The most common participation
      products are tracker certificates, providing 1-to-1 participation to the performance of a basket of securities.
  - language: en
    predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/synonym
    value: participation product
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/StructuredProduct
  - concept: /concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative
resource: https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationInstrument
sources:
- id: fibo-source-f101284000
  resource: references/fibo/DER/DerivativesContracts/StructuredInstruments.rdf
  sha256: f101284000f80ad62d6b30da2f30f5164a9c17d7d55e9b39057d1f085910aa9a
  title: FIBO source DER/DerivativesContracts/StructuredInstruments.rdf
title: participation instrument
type: Ontology Class
---

# participation instrument

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/DER/DerivativesContracts/StructuredInstruments/ParticipationInstrument>

## Definition

structured product that provides the possibility to participate in the performance of an asset or basket of assets

## Relationships

- **Subclass of**: [StructuredProduct](/concepts/fibo/DER/DerivativesContracts/StructuredInstruments/StructuredProduct.md)
- **Subclass of**: [SecurityBasedDerivative](/concepts/fibo/DER/SecurityBasedDerivatives/SecurityBasedDerivatives/SecurityBasedDerivative.md)

## Annotations

- **label** (en): participation instrument
- **definition** (en): structured product that provides the possibility to participate in the performance of an asset or basket of assets
- **adaptedFrom** (en): ISO 10962, Securities and related financial instruments - Classification of financial instruments (CFI) code, Fifth edition, 2021-06-15
- **explanatoryNote** (en): The construction is generally based on a low exercise price option (LEPO) (base value less discounted future dividends) which in some cases might be comparable to a direct investment in the underlying asset(s) or a LEPO combined with other options, which together provide the desired disbursement profile.
- **explanatoryNote** (en): These assets could be anything, from equities, funds, bonds, ETFs indices to a mix of those. The most common participation products are tracker certificates, providing 1-to-1 participation to the performance of a basket of securities.
- **synonym** (en): participation product

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
